=============================
Using grids  module & plugin
=============================



.. sidebar:: Creating grid enabled forms

    .. image:: images/grid-sample.png
       :width: 300px
       :align: center


---------
Goal
---------

The purpose of this example is to show how to build data grids in OPNsense, using the various components
within our framework.

If you haven't read the HelloWorld example yet, we advise you to start there. This example assumes you already know
the basics.

Our topic of choice for this module is a basic list for email addresses, for which you should be able to add, remove and
change items.

--------
Model
--------

Our example starts with a model, which is constructed by creating a php class deriving from :code:`BaseModel` and an XML
file containing the actual model definition.

.. code-block:: php
    :linenos:
    :caption: /usr/local/opnsense/mvc/app/models/OPNsense/GridExample/GridExample.php

    <?php
    namespace OPNsense\GridExample;

    use OPNsense\Base\BaseModel;

    class GridExample extends BaseModel
    {
    }


.. code-block:: xml
    :emphasize-lines: 8, 9, 13
    :linenos:
    :caption: /usr/local/opnsense/mvc/app/models/OPNsense/GridExample/GridExample.xml

    <model>
        <mount>//OPNsense/GridExample</mount>
        <description>
            the OPNsense "GridExample" application
        </description>
        <items>
            <addresses>
                <address type="ArrayField">
                    <enabled type="BooleanField">
                        <default>1</default>
                        <Required>Y</Required>
                    </enabled>
                    <email type="EmailField">
                        <Required>Y</Required>
                    </email>
                </address>
            </addresses>
        </items>
    </model>


Note the :code:`ArrayField` type in the XML, this is a special field type for nested items in automatically includes an internal uuid for easy referencing when written to disk.
Both other field types are also used in the HelloWorld example earlier. All
the preinstalled types can be found in our field type directory on `GitHub <https://github.com/opnsense/core/tree/master/src/opnsense/mvc/app/models/OPNsense/Base/FieldTypes>`__.


----------------------------
API controller
----------------------------

The :code:`ApiMutableModelControllerBase` class supports most model manipulations, all :code:`*Base` methods embody
shared functionality to operate on either new or existing model items.

Our example below uses the base methods to link all operations we need and link them on endpoints ending at :code:`Item`:

* searchItemAction, queries the items in your configuration
* getItemAction, fetches an existing record (or returns a blank one with all defaults)
* addItemAction, add a new record
* setItemAction, update a record
* delItemAction, delete a record
* toggleItemAction, toggle [0|1] the "enabled" property  (see the enabled :code:`BooleanField` in the model)

.. code-block:: php
    :linenos:
    :caption: /usr/local/opnsense/mvc/app/controllers/OPNsense/GridExample/Api/SettingsController.php

    namespace OPNsense\GridExample\Api;

    use \OPNsense\Base\ApiMutableModelControllerBase;

    class SettingsController extends ApiMutableModelControllerBase
    {
        protected static $internalModelName = 'gridexample';
        protected static $internalModelClass = 'OPNsense\GridExample\GridExample';

        public function searchItemAction()
        {
            return $this->searchBase("addresses.address", array('enabled', 'email'), "email");
        }

        public function setItemAction($uuid)
        {
            return $this->setBase("address", "addresses.address", $uuid);
        }

        public function addItemAction()
        {
            return $this->addBase("address", "addresses.address");
        }

        public function getItemAction($uuid = null)
        {
            return $this->getBase("address", "addresses.address", $uuid);
        }

        public function delItemAction($uuid)
        {
            return $this->delBase("addresses.address", $uuid);
        }

        public function toggleItemAction($uuid, $enabled = null)
        {
            return $this->toggleBase("addresses.address", $uuid, $enabled);
        }
    }


The parameters of all methods contain at least the root of the :code:`ArrayField` type you want to operate on
and in cases the action involves form data the name of the root property used as in the container to transport data in.

For example, a getItem (/api/gridexample/settings/getItem/my-uuid-id) would return a response like this (highlighted the container):

.. code-block:: json
    :linenos:
    :emphasize-lines: 2

    {
      "address": {
        "enabled": "1",
        "email": "test@example.com"
      }
    }


----------------------------
Define dialog items
----------------------------

To edit the data we define which fields should be presented to the user and how they are formatted.
Below a simple layout, the id fields reference the actual data points to map (:code:`address.enabled` for example), which is exactly
what the api endpoint returns.

.. code-block:: xml
    :caption: /usr/local/opnsense/mvc/app/controllers/OPNsense/GridExample/forms/dialogAddress.xml

    <form>
        <field>
            <id>address.enabled</id>
            <label>enabled</label>
            <type>checkbox</type>
            <help>Enable this address</help>
        </field>
        <field>
            <id>address.email</id>
            <label>Email</label>
            <type>text</type>
        </field>
    </form>


------------------------------------
Constructing the volt template
------------------------------------

We ship a javascript wrapper to implement a slightly modified version of `jquery-bootgrid <http://www.jquery-bootgrid.com/>`__, to
use this in our template (view) we define three different blocks.

First of all we bind a table by id (grid-addresses) using :code:`UIBootgrid()`, then we define the table which will be
changed into a dynamic searchable grid and finally we link our dialog content using a volt :code:`partial()`.

The basic "UIBootgrid" bind connects all actions which we have defined in our API controller earlier, there are more options
available, but these are not needed for this use-case.

When defining the table, we need to add all fields that should be displayed and the order in which they should appear. If
fields should not be visible by default, simply use :code:`data-visible="false"` on the :code:`<th>` tag.

Our edit dialog is being written in advance so the javascript code can open the statically defined form when needed,
the last highlighted block takes care of this. The partial uses three argument, the variable connected via the
controller containing all form entries, the name (id) of the form, which is referenced in the table (data-editDialog) and
the caption of the dialog.


.. code-block:: html
    :caption: /usr/local/opnsense/mvc/app/views/OPNsense/GridExample/index.volt
    :linenos:
    :emphasize-lines: 3, 14, 37

    <script>
        $( document ).ready(function() {
            $("#grid-addresses").UIBootgrid(
                {   search:'/api/gridexample/settings/searchItem/',
                    get:'/api/gridexample/settings/getItem/',
                    set:'/api/gridexample/settings/setItem/',
                    add:'/api/gridexample/settings/addItem/',
                    del:'/api/gridexample/settings/delItem/',
                    toggle:'/api/gridexample/settings/toggleItem/'
                }
            );
        });
    </script>
    <table id="grid-addresses" class="table table-condensed table-hover table-striped" data-editDialog="DialogAddress">
        <thead>
            <tr>
                <th data-column-id="uuid" data-type="string" data-identifier="true"  data-visible="false">{{ lang._('ID') }}</th>
                <th data-column-id="enabled" data-width="6em" data-type="string" data-formatter="rowtoggle">{{ lang._('Enabled') }}</th>
                <th data-column-id="email" data-type="string">{{ lang._('Email') }}</th>
                <th data-column-id="commands" data-width="7em" data-formatter="commands" data-sortable="false">{{ lang._('Commands') }}</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
        <tfoot>
            <tr>
                <td></td>
                <td>
                    <button data-action="add" type="button" class="btn btn-xs btn-default"><span class="fa fa-plus"></span></button>
                    <button data-action="deleteSelected" type="button" class="btn btn-xs btn-default"><span class="fa fa-trash-o"></span></button>
                </td>
            </tr>
        </tfoot>
    </table>


    {{ partial("layout_partials/base_dialog",['fields':formDialogAddress,'id':'DialogAddress','label':lang._('Edit address')])}}


---------------------------------------
UI controller
---------------------------------------

The user interface controller sets the template (view) to use and collects the dialog form properties from the xml file
defined earlier.

.. code-block:: php
    :linenos:
    :caption: /usr/local/opnsense/mvc/app/controllers/OPNsense/GridExample/IndexController.php

    namespace OPNsense\GridExample;

    class IndexController extends \OPNsense\Base\IndexController
    {
        public function indexAction()
        {
            $this->view->pick('OPNsense/GridExample/index');
            $this->view->formDialogAddress = $this->getForm("dialogAddress");
        }
    }


--------------------------------------
Menu and ACL
--------------------------------------

The sample package on `GitHub <https://github.com/opnsense/plugins/tree/master/devel/grid_example>`__ also contains a
menu definition (xml) and ACL (xml), which are similar to the ones explained in the hello world example.


--------------------------------
Test drive your app
--------------------------------

Now go to http[s]://your.host/ui/gridexample and try it out.

.. image:: images/grid-test-drive.png
   :width: 700px
   :align: center

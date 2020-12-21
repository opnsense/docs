==============================
View construction (and tools)
==============================

Although most of our code base is being processed server side, some things just require interaction on the
clients machine for a fluent user experience.

In this chapter we will try to explain some of the components we use when designing pages and how pages are usually constructed.

--------------------------
Layout
--------------------------

To ease reading of volt templates, we recommend using a fixed layout when creating templates.
The base of our rendered page always contains the standard `layout <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/views/layouts/default.volt>`__
which is hooked via our standard frontend controller.

Below you will find the sections and their order, which we will describe briefly.

.. code-block:: html

    {#
      {1} Copyright notice
    #}
    <script>
    $( document ).ready(function() {
      {2} UI code
    });
    </script>
    {3} page html
    {{ partial("layout_partials/base_dialog",...)}}  {4} dialog forms (see getForm())


#.   The copyright block, 2 clause BSD with the authors on top
#.   Javascript code which belongs to this page
#.   HTML code, usually starts with some :code:`<div>` containers and uses standard Bootstrap 3 layouting
#.   When forms are used, these are placed last, these will be generated to the client as standard html code


----------------------------
ajaxCall
----------------------------

:code:`ajaxCall(url, sendData, callback)` is a wrapper around jQuery's :code:`$.ajax` call preset to a :code:`POST` type
request and wrapping the sendData into a json object.
The :code:`callback` function will be called with the data and status received from the endpoint.



.. code-block:: javascript
    :name: ajaxCall
    :caption: example usage

    ajaxCall('/api/monit/status/get/xml', {}, function(data, status) {
        console.log(data)
    });


----------------------------
ajaxGet
----------------------------

:code:`ajaxGet(url,sendData,callback)` is also a wrapper around jQuery's :code:`$.ajax` call, but for a :code:`GET` type
request.

.. code-block:: javascript
    :name: ajaxGet
    :caption: example usage

    ajaxGet('/api/diagnostics/interface/getInterfaceNames', {}, function(data, status) {
        console.log(data);
    });


----------------------------
mapDataToFormUI
----------------------------

The :code:`mapDataToFormUI(data_get_map, server_params)` can be used to map data retrieved from a controller to a
form in the browser.

This function accepts two parameters, data_get_map contains a mapping between form id's and server endpoints, server_params
is optional and can be used to set option in the :code:`GET` type request.

When the endpoint is successfully called it should return a json type structure containing the path to the item, as an
example using :code:`data_get_map = {'myform': '/api/path/to/formdata'};`:


.. code-block:: json

    {
      "netflow": {
        "capture": {
          "interfaces": {
            "lan": {
              "value": "LAN",
              "selected": 1
            },
            "wan": {
              "value": "WAN",
              "selected": 0
            }
          },
        },
        "collect": {
          "enable": "1"
        }
      }
    }

Which maps to the fields in this simplified structure (usually rendered via our volt templates):

.. code-block:: html

    <form id="myform">
        <select multiple="multiple" id="netflow.capture.interfaces">
        </select>
        <input type="checkbox" id="netflow.collect.enable">
    </form>


The function returns a :code:`$.Deferred()` which will be resolved when all endpoints are called.

----------------------------
saveFormToEndpoint
----------------------------

:code:`saveFormToEndpoint(url, formid, callback_ok, disable_dialog, callback_fail)` is the opposite of :code:`mapDataToFormUI()`
and retrieves the data from the form and sends it to the configured (url) endpoint as json structure.

The response data looks similar to the example data in mapDataToFormUI, but more condensed since selections will
be returned as single (separated) values, such as :code:`lan,wan` if both options where set.


----------------------------
updateServiceControlUI
----------------------------

The code:`updateServiceControlUI(serviceName)` function hooks the service control on top of the standard template, where you can find
the [re]start, stop and status of the service.

It assumes the following endpoints exists for the module:

* /api/{{serviceName}}/service/status
    * returns the status of the service (running, stopped) in a field named "status"
* /api/{{serviceName}}/service/start
    * start the service
* /api/{{serviceName}}/service/restart
    * restart the service
* /api/{{serviceName}}/service/stop
    * stop the service


----------------------------
Dialog wrappers
----------------------------

We are using `BootstrapDialog <https://nakupanda.github.io/bootstrap3-dialog/>`__ to display standard dialogs, to limit
the boilerplates needed to show these dialog we added the following wrapper funcitons:


stdDialogInform(title, message, close, callback, type, cssClass)
..............................................................................................

Informational dialog with a single close button, using the following parameters:

*   title: :code:`string` dialog title
*   message: :code:`string` dialog message
*   close:  :code:`string` close button text
*   callback: :code:`function()` to be called after close
*   type: :code:`string` dialog type. one of : danger, default, info, primary, success, warning
*   cssClass: :code:`string`  css class to use


stdDialogConfirm(title, message, accept, decline, callback, type)
..............................................................................................

Ok/Cancel dialog type using the following parameters:

*   title: :code:`string` dialog title
*   message: :code:`string` dialog message
*   accept:  :code:`string` accept button text
*   decline:  :code:`string` decline button text
*   callback: :code:`function()` to be called after close
*   type: :code:`string` dialog type. one of : danger, default, info, primary, success, warning



stdDialogRemoveItem(message, callback)
..............................................................................................

Simple remove item (warning) dialog, using a message and optionally a callback.

----------------------------
$.SimpleActionButton
----------------------------

Using the jQuery extension :code:`SimpleActionButton` one can register simple ajax calls on components click events, which
will call the selected endpoint and show a progress animation (spinner) to the user.

The following parameters can be supplied as data attributes on the target object:

* endpoint : endpoint to call (e.g. :code:`/api/my/action`)
* label : button label text
* service-widget : the service widget to refresh after execution, see :code:`updateServiceControlUI()`
* error-title : error dialog title

The method itself can be feed with callbacks to call before (:code:`onPreAction()`) and after (:code:`onAction()`) execution.

An example of a button could look like this:

.. code-block:: html

    <button class="btn btn-primary" id="reconfigureAct"
            data-endpoint='/api/component/service/reconfigure'
            data-label="{{ lang._('Apply') }}"
            data-service-widget="component"
            data-error-title="{{ lang._('Error reconfiguring component') }}"
            type="button"
    ></button>

To utilize the callbacks, one could use:

.. code-block:: html

    $('#btnTest').SimpleActionButton({
        onPreAction: function() {
            const dfObj = new $.Deferred();
            console.log("called before endpoint execution, returning a promise.");
            return dfObj;
        },
        onAction: function(data, status){
            console.log("action has been executed.");
        }
    });


----------------------------
$.UIBootgrid
----------------------------

The UIBootgrid jQuery extension is a wrappper around a slightly modified `jquery-bootgrid <http://www.jquery-bootgrid.com/>`__
component, the pattern we implement with our wrapper is inspired by `this <http://www.jquery-bootgrid.com/Examples#command-buttons>`__ example.


Defining the html table is best explained in the jquer-bootgrid examples, our wrapper eases the implementation of the javascript code.

The minimal implementation contains a reference to the search endpoint which should return a json resultset containing :code:`rows`
and pagination data (:code:`current`, :code:`rowCount`, :code:`total`).

.. code-block:: html

  $("#my_grid").UIBootgrid(
      {   search:'/api/path/to/search',
          get:'/api/path/to/get',
          set:'/api/path/to/set',
          add:'/api/path/to/add',
          del:'/api/path/to/del',
          toggle:'/api/path/to/toggle',
          info:'/api/path/to/info'
      }
  );


The other optional endpoints are either used to populate a form, as defined in the :code:`data-editDialog` property on the table or
can be used to feed actions, such as **set** (set new values, return validation errors), **add** a new record, **del**  an existing record
or **toggle** if the record should be enabled or disabled.  :code:`info` endpoints are not used very often (and can safely be omitted), these are mainly intended as simple trigger to display an info dialog.


A full example of a baisc grid is available in our  :doc:`../examples/using_grids` example

In some cases the developer wants to signal the user about the fact that changes need to be applied in order to be active, for this scenario one can use the :code:`data-editAlert`
property of the table, which offers the ability to show an alert after changes. Below example would be shown when the table tag contains :code:`data-editAlert="exampleChangeMessage"`

.. code-block:: html

    <div id="exampleChangeMessage" class="alert alert-info" style="display: none" role="alert">
        {{ lang._('After changing settings, please remember to apply them with the button below') }}
    </div>


.. Tip::

    You can access the general settings of the jquery-bootgrid plugin using the :code:`options` property, which can be convenient when you would like to change
    requests or responses as being exchanged with the server. The available options are described `here <http://www.jquery-bootgrid.com/Documentation#table>`__


OPNsense settings
.......................

We added a couple of setttings to the list, which help to extend our plugin a bit more easily. Below we will explain which settings (within the options tag) are added by us:

*   useRequestHandlerOnGet

    *   Boolean value which enables the use of the request handler when a :code:`get` request is executed ot fetch data for the dialog. This can be used to add parameters to the request.

*   onBeforeRenderDialog

    *   function handler which will be called before an edit dialog is being displayed, can be used to change the otherwise static dialogs. Should return a $.Deferred() object. (e.g. :code:`return (new $.Deferred()).resolve();`)


Formatters
.......................

Formatters can be used in the grid heading to choose the presentation of an attribute, we include a couple of standard formatters which are:

*   commands (commands list, edit,copy and delete)
*   commandsWithInfo (same as commands, but with an info button as well)
*   rowtoggle (show enabled status and act as toggle button)
*   boolean (show boolean value)



Visible columns
......................

jquery-bootgrid offers the ability to add columns which are not visible by default using the :code:`data-visible` tag. When
using our wrapper, these can be used to set defaults as well,
but the users last selection is also recorded in its local browser storage as well as the number of results shown in the grid when opening the same page again.

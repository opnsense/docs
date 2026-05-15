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
Underneath this function uses :code:`getFormData(parent)` defined in `opnsense.js` which is responsible for extracting values from
different form types such as :code:`<input>` and :code:`<select>` types. When the attributes should be type safe
(e.g. an *integer* in json format should be presented as :code:`1` and not as :code:`"1"`),
there is the possibility to "cleanse" the data first using a filter.  In this case define an attribute on the input tag with the name :code:`type_formatter`
containing the function to call.


.. code-block:: html

    <input type="text" type_formatter="my_convert_to_int_function" id="myform.myintval">

Which could be implemented in the form javascript as:

.. code-block:: javascript

    function my_convert_to_int_function(payload)
    {
        if (/^[+-]?[0-9]*$/.test(payload)) {
            return  parseInt(payload);
        } else {
            return payload;
        }
    }

The response data looks similar to the example data in mapDataToFormUI, but more condensed since selections will
be returned as single (separated) values, such as :code:`lan,wan` if both options where set.

Using the example with the function above, a valid integer would offer a json object similar to :code:`{"myform": {"myintval": 1}}`,
unparsable data would look like :code:`{"myform": {"myintval": "1x"}}`, in which case backend validations are able to feedback validation results.


----------------------------
updateServiceControlUI
----------------------------

The :code:`updateServiceControlUI(serviceName)` function hooks the service control on top of the standard template, where you can find
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
the boilerplates needed to show these dialog we added the following wrapper functions:


stdDialogInform(title, message, close, callback, type, cssClass)
..............................................................................................

Informational dialog with a single close button, using the following parameters:

*   title: :code:`string` dialog title
*   message: :code:`string` dialog message
*   close:  :code:`string` close button text
*   callback: :code:`function()` to be called after close
*   type: :code:`string` dialog type. one of: danger, default, info, primary, success, warning
*   cssClass: :code:`string`  css class to use


stdDialogConfirm(title, message, accept, decline, callback, type)
..............................................................................................

Ok/Cancel dialog type using the following parameters:

*   title: :code:`string` dialog title
*   message: :code:`string` dialog message
*   accept:  :code:`string` accept button text
*   decline:  :code:`string` decline button text
*   callback: :code:`function()` to be called after close
*   type: :code:`string` dialog type. one of: danger, default, info, primary, success, warning



stdDialogRemoveItem(message, callback)
..............................................................................................

Simple remove item (warning) dialog, using a message and optionally a callback.

.. _simpleactionbutton:

----------------------------
$.SimpleActionButton
----------------------------

Using the jQuery extension :code:`SimpleActionButton` one can register simple ajax calls on components click events, which
will call the selected endpoint and show a progress animation (spinner) to the user.

The following parameters can be supplied as data attributes on the target object:

* endpoint: endpoint to call (e.g. :code:`/api/my/action`)
* label: button label text
* service-widget: the service widget to refresh after execution, see :code:`updateServiceControlUI()`
* error-title: error dialog title

The method itself can be fed with callbacks to call before (:code:`onPreAction()`) and after (:code:`onAction()`) execution.

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

``SimpleActionButton`` will also show a reminder to the user to save their settings if prompted. To do so,
simply call :code:`$(document).trigger("settings-changed");`.

.. _simplefileuploaddlg:

----------------------------
$.SimpleFileUploadDlg
----------------------------

The simple file upload dialog can be used to select a file and upload it to a specified endpoint.

To define a button sending data to `/api/path/to/import_controller`, the following code could be used:

.. code-block:: html

    <button
        id="upload"
        type="button"
        data-title="Import"
        data-endpoint='/api/path/to/import_controller'
        class="btn btn-xs"
    ><span class="fa fa-fw fa-table"></span></button>


.. Note::

    The structure of this :code:`POST` contains a :code:`payload` and a :code:`filename` property.

Initializing this button could be done using:

.. code-block:: html

    $("#upload").SimpleFileUploadDlg();


.. Tip::

    The :code:`SimpleFileUploadDlg` action supports an :code:`onAction` handler similar to the one described in :code:`$.SimpleActionButton`


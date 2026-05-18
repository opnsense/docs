==============================
UIBootgrid
==============================

The UIBootgrid system is a wrapper around `Tabulator <https://tabulator.info/>`__ and provides
a generic table system that is reusable on all pages requiring data listing and manipulation.


Setup
------------

To get started, see :doc:`../examples/using_grids`. The example will show you how to get started
with a minimal grid setup and how this front-end code ties to the controller layer.


Basic Layout
------------

Since the controller layer defines standardized output and expects standardized input, it's
possible to construct and feed a grid by simply defining a set of endpoints as explained in the setup:

.. code-block:: javascript

    $("#{{formGridAddress['table_id']}}").UIBootgrid(
        {   
            search:'/api/gridexample/settings/search_item/',
            get:'/api/gridexample/settings/get_item/',
            set:'/api/gridexample/settings/set_item/',
            add:'/api/gridexample/settings/add_item/',
            del:'/api/gridexample/settings/del_item/',
            toggle:'/api/gridexample/settings/toggle_item/',
            info:'/api/gridexample/settings/info'
        }
    );

You can use the browser developer tool to inspect the request/response structures of each
operation. For example, the :code:`search` endpoint looks like this:

**Request:**

.. code-block:: javascript

    {
        "current": 1,
        "rowCount": 50,
        "sort": {}
    }


**Response:**

.. code-block:: javascript

    {
        "rows": [
            {
                "uuid": "3b4e949d-443b-4127-a709-1e41589db462",
                ...
            },
            ...
        ],
        "rowCount": 1,
        "total": 1,
        "current": 1
    }

.. Note::

    :code:`info` endpoints are not used very often (and can safely be omitted),
    these are mainly intended as simple trigger to display an info dialog.


Configuration Reference
-----------------------

The :code:`UIBootgrid` initialization object starts with the CRUD methods as stated above, but
the whole structure contaions a lot of options to modify the behavior to fit your purpose.

The top-level options are layed out as follows:

.. code-block:: text

   config
   ├── search
   ├── get
   ├── set
   ├── add
   ├── del
   ├── toggle
   ├── info
   ├── options
   │   ├── ...
   │   ├── ...
   │   └── ...
   ├── commands
   │   ├── ...
   │   └── ...
   ├── tabulatorOptions
       ├── ...
       └── ...


``options``
-----------

General settings for bootgrid behavior

.. list-table::
   :header-rows: 1
   :widths: 20 20 15 45

   * - Property
     - Type
     - Default
     - Description
   * - ``datakey``
     - ``string``
     - ``"uuid"``
     - Defines the property in the data that is used for indexing into the grid. Since most
       model data is uniquely identified through a UUID, this property defaults to
       :code:`uuid`. However, in some situations you may wish to override this if the data
       uses a different key.
   * - ``disableScroll``
     - ``boolean``
     - ``false``
     - Disables in-grid vertical scrolling behavior. Setting this to :code:`true` means
       all rows will be rendered if not constrained by pagination, so be aware of the performance
       impact if your grid contains many rows.
   * - ``sorting``
     - ``boolean``
     - ``true``
     - Whether sorting should be enabled. Sorting is triggered through header clicks.
   * - ``rowCount``
     - ``array``
     - ``[50, 100, 200, 500, 1000, true]``
     - An array of numbers that defines the selection of row counts a user can select.
       The special value :code:`true`, means "all rows".
   * - ``formatters``
     - ``object``
     - ``Internal formatters``
     - Formatters for values in cells. See :ref:`formatters`.
   * - ``headerFormatters``
     - ``object``
     - ``{}``
     - Formatters for the headers of columns. See :ref:`headerFormatters`.
   * - ``statusMapping``
     - ``object``
     - ``{}``
     - A key-value pair representing status colors. For example:

       .. code-block:: javascript

        statusMapping: {
            0: "fw-pass",
            1: "fw-nat",
            2: "fw-block",
        }

       To use this, each row must contain a :code:`status` property set to one
       of the keys defined in the status mapping. UIBootgrid will automatically
       add the value as a class to the cell element. The values must be valid classes
       defined in CSS. This is mainly used to give rows a specific background
       color based on their status.
   * - ``sorters``
     - ``object``
     - ``Internal sorters``
     - Specify one or more custom sorter functions indexed by key. To instruct
       a column to use this sorter, set the :code:`sorter` property through
       the :code:`grid_view` tag as explained in :ref:`define-dialog-items`.
       These sorters are only applied if :code:`ajax: false`, meaning that
       all sorting logic happens locally.
   * - ``requestHandler``
     - ``function``
     - ``null``
     - Request handler callback function that's executed before the AJAX call.

       The function expects 1 parameter: :code:`params` and must return this same
       parameter. This parameter is an object that contains all data to be sent to
       the endpoint. With this function you may modify/override the data sent to
       the endpoint before it's sent.
   * - ``responseHandler``
     - ``function``
     - ``null``
     - Response handler callback function that's executed after AJAX response.
       This function expects 1 parameter: :code:`response` and must return this
       same parameter. This parameter contains the response from the called endpoint.
       You may use this function to modify/override the response before it's used by
       the grid system.
   * - ``resetButton``
     - ``boolean``
     - ``true``
     - Determines if the grid reset button should be rendered. The grid locally persists
       certain changes by default, such as column resizes, sorting behavior etc. This
       button clears the persistence and resets the grid to all defaults.
   * - ``searchSettings``
     - ``object``
     - ``{delay: 1000}``
     - Allows modifying search behaviour of the grid. Currently only "delay" is defined
       and set to 1000ms by default. Delay is the amount of time waiting before reloading
       the grid after search.
   * - ``navigation``
     - ``boolean``
     - ``true``
     - If the action bar, pagination and footer should be rendered.
   * - ``ajax``
     - ``boolean``
     - ``true``
     - If disabled, ignores any CRUD endpoint defined. Use the :ref:`replace` or
       :ref:`append` functions to add data to the grid yourself. If disabled, any sorting,
       filtering or pagination will happen locally, as all data is expected to be present
       in the grid. You can use the :code:`sorters` to define sorting logic yourself.

       If enabled, uses the defined CRUD enpoints to fetch/filter/sort and modify
       the data.
   * - ``ajaxConfig``
     - ``object``
     - See description
     - Ajax configuration used in all ajax calls. The defaults are:

       .. code-block:: javascript

        {
            method: "POST",
            dataType: "json",
            headers: {
                "Content-type": "application/json;charset=utf8"
            }
        }
      
       Override for advanced purposes.
   * - ``responsive``
     - ``boolean``
     - ``false``
     - If this grid is allowed to split longer lines into newlines, creating variable height
       grid rows. Use this if the cell content should always be visible, otherwise, the content
       will be cut off with an ellipsis and dynamically assigned a tooltip so hovering over
       the data will show the full content.
   * - ``onBeforeRenderDialog``
     - ``function``
     - ``null``
     - function handler which will be called before an edit dialog is being displayed, can
       be used to change the otherwise static dialogs. Should return a $.Deferred() object.
       (e.g. :code:`return (new $.Deferred()).resolve();`)
   * - ``virtualDOM``
     - ``boolean``
     - ``false``
     - Enable or disable the virtual rendering mode of the grid. See
       `the Tabulator docs <https://tabulator.info/docs/6.4/virtual-dom>`__. In essence
       this option makes sure that not all rows are rendered by default, but are rendered
       on the fly as they are needed when the user scrolls down/up. This makes it possible
       to render an extremely large amount of rows with very little performance impact.

       When using this options, keep in mind that each row may not be available in the DOM
       yet at any given time for direct referencing in code. Therefore, the proper
       :code:`onRendered` callbacks should be used if you wish to refer to this element
       directly. See :ref:`formatters` and :ref:`commands`.
   * - ``selection``
     - ``boolean``
     - ``true``
     - Whether individual rows should be selectable through a checkbox in a left-frozen column.
   * - ``multiSelect``
     - ``boolean``
     - ``true``
     - Whether multiple rows may be selected for actions
       (:code:`delete-selected`, :code:`enable-selected`, :code:`disable-selected`).
       Only relevant if :code:`selection: true`
   * - ``stickySelect``
     - ``boolean``
     - ``false``
     - Ignores :code:`multiSelect`. Enable this if selecting a row should disable the selection
       of another row, forcing exactly one row to be selected at all times. This is often
       used in master-detail views, where one row corresponds to the entries in another
       grid. Only relevant if :code:`selection: true`
   * - ``rowSelect``
     - ``boolean``
     - ``false``
     - Whether rows should be selectable by clicking in any of the row cells. Keep in mind that
       in UX terms, this makes it difficult for users to select values in a grid for copy+pasting
       purposes.
   * - ``batchToggle``
     - ``boolean``
     - ``true``
     - Enable/disable the batching of the :code:`enable/disabled-selected` actions. Batching involves
       taking all of the :code:`datakey` strings of the selected rows and splitting these up into
       :code:`batchToggleSize`-length chunks, and firing one toggle request per batch.
       The request contains all :code:`datakey` strings as a single comma-separate parameter.
       Therefore, the controller should be capable of dealing with these keys
       (:code:`toggleBase`). Set this to :code:`false` only if your controller endpoint
       is not capable of dealing with multiple values in one request.
   * - ``batchToggleSize``
     - ``number``
     - ``40``
     - Default maximum batch side for :code:`batchToggle`. This number roughly corresponds
       to the length of a single UUID * 40 to keep the length of a URL below its maximum.
       Adjust this number if the :code:`datakey` is not a UUID.
   * - ``batchDelete``
     - ``boolean``
     - ``true``
     - Enable/disable the batching of the :code:`delete-selected` action. Batching involves
       taking all of the :code:`datakey` strings of the selected rows and splitting these up into
       :code:`batchDeleteSize`-length chunks, and firing one delete request per batch.
       The request contains all :code:`datakey` strings as a single comma-separate parameter.
       Therefore, the controller should be capable of dealing with these keys.
       Set this to :code:`false` only if your controller endpoint
       is not capable of dealing with multiple values in one request.
   * - ``batchDeleteSize``
     - ``number``
     - ``40``
     - Default maximum batch side for :code:`batchDelete`. This number roughly corresponds
       to the length of a single UUID * 40 to keep the length of a URL below its maximum.
       Adjust this number if the :code:`datakey` is not a UUID.
   * - ``triggerEditFor``
     - ``string``
     - ``null``
     - Set this value to a :code:`datakey` value (such as a UUID) to trigger the edit dialog
       of this particular row. This is used in cases where we are referred to from a different
       page to load both the grid and immediately open the right entity for editing.

       If we came from a different page, the :code:`edit` URL parameter will be set to the
       :code:`datakey` value. This parameter can be fetched through :code:`getUrlHash('edit')`.

       In most cases, if triggering an edit on referral is necessary, :code:`getUrlHash('edit')`
       should be used. If the referrer sets a different URL parameter, adjust your logic
       accordingly.
   * - ``initialSearchPhrase``
     - ``string``
     - ``null``
     - Same behaviour as :code:`triggerEditfor`, but for a search phrase value. If set,
       the grid will load with the search value set to this string so the controller
       can filter on it.

       The standardized method to get this value is :code:`getUrlHash('search')`.
   * - ``static``
     - ``boolean``
     - ``false``
     - Disables persistent storage and resizable columns so the dimensions of the grid are
       predictable at all times.
   * - ``bottomReserveElement``
     - ``string | Element | JQuery object``
     - ``'.grid-bottom-reserve''``
     - If there is an element below the grid that should be visible at all times (no page scrollbar),
       you can specify this element here so the grid height calculation takes the height of
       this element into account.


.. _formatters:

``options.formatters``
----------------------

Formatters are functions that are executed for each cell whose column has a formatter specified
and determine the value that is presented to the user in the cell. Formatters allow you
to manipulate the data fetched from the controller into a format that is more easily digestable
for a user.

The :code:`formatters` option is an object that contains :code:`key` - :code:`function` pairs,
where each key corresponds to the :code:`formatter` value in the grid form as explained in
:ref:`define-dialog-items`.

For example:

.. code-block:: javascript

    formatters: {
        myformatter: function (column, row, onRendered) {
            return row[column.id];
        }
    }

The above example simply returns the value of the row without modifications.

The :code:`column` parameter is an object that contains the :code:`id` and the :code:`visibility`
status of the column.

The :code:`row` parameter is an object that contains the data for this row.

The :code:`onRendered` parameter is a callback function that allows you to execute a function
when the cell has been rendered. For example:

.. code-block:: javascript

    formatters: {
        myformatter: function (column, row, onRendered) {
            onRendered((cell) => {
                console.log(`grid cell has been rendered. cell data: ${cell.getData()}`);
            })
            return row[column.id];
        }
    }

This is useful if you want to bind event handlers to the rendered DOM element, or do work
if the cell contains more complex objects such as graphs that are initialized asynchronously.

The callback function expects a single parameter, :code:`cell`, which you can access to get the
`cell object <https://tabulator.info/docs/6.4/components#component-cell>`__

.. _headerFormatters:

``options.headerFormatters``
----------------------------

Functionally equivalent to :ref:`formatters`, but applied to the column header value instead.
By default it's not necessary to specify a :code:`headerFormatter` tag in the :code:`grid_view`
tag of a form, as the keys match to the row keys. For example:

.. code-block:: javascript

    headerFormatters: {
        enabled: function(column) {
            return '<i class="fa-solid fa-fw fa-check-square" data-toggle="tooltip" title="{{ lang._('Enabled') }}"></i>';
        }
    }

The above example will match on the :code:`enabled` row key and return an icon with a tooltip
showing the translated value of the column title.

The function expects only a single parameter, :code:`column`, which is an object containing
:code:`id`, :code:`visible`, :code:`title`.

.. _commands:

``commands``
----------------------------

The :code:`Commands` column is a special column that is situated frozen on the right side of the grid
to ease access regardless of scroll position. This column contains buttons that are linked to actions
that can be defined/extended in this configuration section.

Besides the commands defined in the commands column, there are also command buttons placed below the grid
which are linked to actions that are not related to one grid row specifically, such as :code:`add` or
:code:`delete-selected`. These buttons can also be defined in the command structure, but with the
:code:`footer` property set to :code:`true`.

The following commands are built-in by default and are rendered automatically based on their respective
CRUD endpoint requirements:

- ``add``. Requires ``get``, ``set``.
- ``edit``. Requires ``get``, ``set``.
- ``delete``. Requires ``del``.
- ``copy``. Requires ``get``, ``sets``.
- ``info``. Requires ``info``,
- ``toggle``. Requires ``toggle``.
- ``enable-selected``. Requires ``toggle`` (See ``batchToggle`` option).
- ``disable-selected``. Requires ``toggle`` (See ``batchToggle`` option).
- ``delete-selected``. Requires ``del`` (See ``batchDelete`` option).

You may override a specific property of the above built-in commands, as the ``commands`` object
is deeply merged, e.g.:

.. code-block:: javascript

    edit: {
        sequence: 200
    }

Will preserve all :code:`edit` command options, but change the sequence from its default of ``100``
to ``200``.

Extra commands can be defined in the top-level :code:`commands` object. The structure of a command starts
with a unique key and contains an object with the following schema:

.. list-table::
   :header-rows: 1
   :widths: 20 20 15 45

   * - Property
     - Type
     - Required
     - Description
   * - ``method``
     - ``function``
     - No
     - A function that is executed on command click. Function signature is :code:`(event, cell)`.
       The `cell object <https://tabulator.info/docs/6.4/components#component-cell>`__ is passed in
       only if :code:`footer` is :code:`false`.
   * - ``title``
     - ``string | function``
     - No
     - Translated title to be shown as a tooltip. If the title depends on state, this property can also
       be a function. If it's a function, the Cell object is passed as a parameter.
   * - ``requires``
     - ``array``
     - No
     - An optional array of strings that define if this command depends on one or more CRUD actions.
       For example, the default :code:`add` command depends on :code:`get` and :code:`set`,
       otherwise the form logic tied to this action wouldn't be able to get the structure needed to construct
       the form, nor would it be able to call the right endpoint once "save" has been clicked. If any
       of the required endpoints are missing, the button isn't rendered.
   * - ``sequence``
     - ``number``
     - No
     - A number to control how the button is ordered amongst the other buttons.
   * - ``footer``
     - ``boolean``
     - No
     - Whether this command should be rendered in the footer or as part of a row.
   * - ``primary``
     - ``boolean``
     - No
     - Whether this command should be rendered as part of the primary button container.
       Only relevant when :code:`footer` is :code:`true`.
   * - ``classname``
     - ``string``
     - Yes
     - Icon class added to the :code:`<span>` inside the button element.
   * - ``filter``
     - ``function``
     - No
     - A function that, if defined, must return true or false and determines if this command
       should be rendered. The Cell object is only passed in if :code:`footer` is :code:`false`.
   * - ``onRendered``
     - ``function``
     - No
     - A function that runs after the element including event bindings have been rendered.
       This allows the caller to override the behavior of the command. The element is bound to the function
       and can be access through :code:`$(this)`, but the full Cell object is passed in as a parameter
       as well, but only if :code:`footer` is :code:`false`. This function has priority over :code:`method`.

       This function can be used to bind the rendered command DOM element to other system
       components, such as :ref:`simplefileuploaddlg`.

There are default commands built-in to the UIBootgrid framework that work in tandem with the
default controller actions to facilitate basic CRUD behavior.

For advanced use cases, you can also call the built-in :code:`command` methods directly. For an
example, see the
`Unbound overrides template <https://github.com/opnsense/core/blob/master/src/opnsense/mvc/app/views/OPNsense/Unbound/overrides.volt>`__


``tabulatorOptions``
--------------------

Any option set here will be passed directly to Tabulator. Refer to their `docs <https://tabulator.info/docs/>`__.


Methods
-------

Methods on UIBootgrid can be called through the JQuery bootgrid API:

.. code-block:: javascript
    
    $('#<grid-id>').bootgrid('<method>', ...params);



.. _append:

``append(rows)``
~~~~~~~~~~~~~~~~

Appends ``rows`` to the grid. This is a lot slower than :ref:`replace`. Since most of the sorting/filtering
logic happens remotely, :code:`replace` should be the preferred method to manipulate data
in the grid.

.. _replace:

``replace(rows)``
~~~~~~~~~~~~~~~~~

Replaces all data in the grid by ``rows``. Use this function if :code:`ajax: false` to set data in the grid.

``getTable()``
~~~~~~~~~~~~~~

Gets the Tabulator grid instance bound to this :code:`UIBootgrid`.

``clear()``
~~~~~~~~~~~

Clears any data in the grid.

``reload()``
~~~~~~~~~~~~

Reload the grid. Triggers a new AJAX request. Always use this


``getRowCount()``
~~~~~~~~~~~~~~~~~

Gets currently selected row count

``getSelectedRows()``
~~~~~~~~~~~~~~~~~~~~~

Gets the :code:`datakey` values of the currently selected rows

``getCurrentRows()``
~~~~~~~~~~~~~~~~~~~~

Gets all :code:`datakey` values of all rows in the table

``getCurrentPage()``
~~~~~~~~~~~~~~~~~~~~

Gets current paginated page.

``destroy()``
~~~~~~~~~~~~~

Destroy the grid

``setColumns(columns)``
~~~~~~~~~~~~~~~~~~~~~~~

Enable the visibility of columns. The :code:`columns` parameter expects an
array of column IDs.

``unsetColumns(columns)``
~~~~~~~~~~~~~~~~~~~~~~~~~

Disable the visibility of columns. The :code:`columns` parameter expects an
array of column IDs.

``search(value, event)``
~~~~~~~~~~~~~~~~~~~~~~~~

Search for :code:`value` in the grid (triggering an AJAX request if :code:`ajax: true`).

``select(ids)``
~~~~~~~~~~~~~~~

Programatically select rows. Expects an array of :code:`datakey` strings.

``getSearchPhrase()``
~~~~~~~~~~~~~~~~~~~~~

Get current search phrase.

``setPersistence(value)``
~~~~~~~~~~~~~~~~~~~~~~~~~

Enable or disable grid persistence (column setup in local storage). Expects a boolean.


Other components
----------------

If an ``apply`` button is rendered on the page through :ref:`simpleactionbutton`, :``UIBootgrid``
will automatically signal to that element to prompt the user to apply if something in the grid changed,
e.g. when a row has been edited. Internally it does this by simply calling :code:`$(document).trigger("settings-changed");`.

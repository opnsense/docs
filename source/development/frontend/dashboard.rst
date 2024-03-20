=================
Dashboard widgets
=================

-------
General
-------

OPNsense provides an easy framework for developing dashboard widgets within a simple abstraction layer.
Each widget is a separate Javascript module that extends from a base widget class. Each widget exposes a set of functions
that are called by the dashboard framework logic. Each widget class also exposes the API endpoints it uses to fetch
data, so that the dashboard controller can apply per-widget ACL checks.

The framework provides the following features:

- A responsive and dynamic grid that allows the user to build up a custom layout.
- The layout can be saved per logged in user.
- Administrators that restrict access to specific pages for specific users will automatically restrict
  access to the widgets that also use the same data feed.
- Widgets are fully asynchronous, meaning they are fully independent from one another, making sure that resource intensive
  widgets will not hold up other widgets.

This framework uses `GridStack <https://gridstackjs.com/>`__ to create the dashboard grid.

Widgets are placed in the :code:`src/opnsense/www/js/widgets/` directory.

A complete example of a simple widget can be found `here <https://github.com/opnsense/core/blob/master/src/opnsense/www/js/widgets/Interfaces.js>`__

-------
Example
-------

Before going into any details, it is often most useful to present an example that includes most of the core logic:
the `interfaces overview <https://github.com/opnsense/core/blob/master/src/opnsense/www/js/widgets/Interfaces.js>`__ widget.

---
ACL
---

Every widget must expose the endpoints it's using to the framework, so the controller can determine whether
this widget is accessible for the current logged in user. To do this, any :code:`<widget>.js` file must start
with the following line(s):

.. code-block:: javascript

    // endpoint:/api/endpoint/used/by/widget

For example:

.. code-block:: javascript

    // endpoint:/api/interfaces/overview/*

Multiple lines can be used if the widget uses multiple endpoints. If any of these endpoints are inaccessible,
the widget will not be loaded. Note that the same rules as for any other
`ACL <../../development/examples/helloworld.html#plugin-to-access-control-acl>`__ applies here.

---------
Functions
---------

The `BaseWidget <https://github.com/opnsense/core/blob/master/src/opnsense/www/js/widgets/BaseWidget.js>`__ shows the skeleton
of the widget Javascript module. Widgets extend this class to provide defaults to the framework. To make life a little
easier for common patterns, other base widgets may also be exposed. Currently this is only the
`BaseTableWidget <https://github.com/opnsense/core/blob/master/src/opnsense/www/js/widgets/BaseTableWidget.js>`__
which exposes a dynamic table that can be configured in multiple orientations and only needs a data feed.

The following functions are available to be overridden by the widget:

*Constructor*
=====================================================================================================================

.. code-block:: javascript

    constructor(config) {}

To provide sensible defaults to the framework, a derived javascript class should always call :code:`super()` first in the constructor.
Afterwards, the defaults can be overridden. The properties are:

- :code:`this.title`. Sets the title of the widget in the header.
- :code:`this.tickTimeout`. Sets the interval (in ms) in which the :code:`onWidgetTick()` function is called. The default is 5000

If the widget has been persisted (the user pressed 'save'), the loaded widget configuration is passed in the constructor. Any
custom data necessary for the widget to properly reload itself can be found in the :code:`this.config` property, if any.

*getGridOptions*
=====================================================================================================================

.. code-block:: javascript

    getGridOptions() {}

To provide flexibility, the widget can optionally override this function and return an object that will be merged and loaded
into the GridStack API. This function is called before the widget is rendered to the DOM. For example, the following code:

.. code-block:: javascript

    getGridOptions() {
        return {
            // trigger overflow-y:scroll after 650px height
            sizeToContent: 650
        }
    }

will insert the :code:`sizeToContent: 650` key-value pair into the GridStack options, making sure that the height of the widget
does not exceed a maximum of 650 pixels before a scrollbar is inserted. The GridStack API reference can be found
`here <https://github.com/gridstack/gridstack.js/blob/master/doc/README.md>`__.

This object is also persisted once the dashboard has been saved, meaning these properties are also passed in the constructor
on a widget reload.

The properties do not have to correspond to the GridStack API, any custom data can be pushed here.

*getMarkup*
=====================================================================================================================

.. code-block:: javascript

    getMarkup() {}

This function must return a jQuery object that contains the static markup that's necessary to build the layout
of the widget. This function will usually just return the container (with styling attached) where dynamic content
will be loaded using `onMarkupRendered()`

*onMarkupRendered*
=====================================================================================================================

.. code-block:: javascript

    async onMarkupRendered() {}

As soon as the dashboard has loaded, and all widget markup has been rendered to the DOM, dynamic content can be
provided to fill the widget by defining this function. Since this is an :code:`async` function, any API call
within this function must be awaited. For example:

.. code-block:: javascript

    async onMarkupRendered() {
        await ajaxGet('/api/interfaces/overview/interfacesInfo', {}, (data, status) => {
            // do something with the data
        });
    }

This will make sure that all other widgets remain responsive, and a spinner appears while the data is being loaded.
Use jQuery to update the markup as prepared by :code:`getMarkup()`.

*onWidgetResize*
=====================================================================================================================

.. code-block:: javascript

    onWidgetResize(elem, width, height) {}

If a widget is resized by the user, or is resized due to layout constraints / browser resize, this function will be called
with the updated width and height. The widget element is passed into the function as well.

Use this function to keep the widget responsive and the layout coherent for different sizes. For example:

.. code-block:: javascript

    onWidgetResize(elem, width, height) {
        if (width > 500) {
            $('.interface-info-detail').parent().show();
            $('.interface-info').css('justify-content', 'initial');
            $('.interface-info').css('text-align', 'left');
        } else {
            $('.interface-info-detail').parent().hide();
            $('.interface-info').css('justify-content', 'center');
            $('.interface-info').css('text-align', 'center');
        }
    }

The above code will make sure that if the width of the widget is less than 500px wide, less critical
information is removed. Adjust the styling as necessary.

.. warning::

    While this function is debounced (throttled to prevent excessive calls), it is still executed often during a resize.
    If this function is doing a lot of heavy lifting, make sure you implement a notion of state to prevent
    the same logic from executing more than necessary. An example of this can be found in the
    `BaseTableWidget <https://github.com/opnsense/core/blob/master/src/opnsense/www/js/widgets/BaseTableWidget.js>`__.

If you return true from this function, the grid will be forcefully updated to adjust to a new layout.

*onWidgetTick*
=====================================================================================================================

.. code-block:: javascript

    onWidgetTick() {}

This function is called every :code:`this.tickTimeout` milliseconds. While the dashboard is open, this function
is used to update the data presented on the dashboard.

*onWidgetClose*
=====================================================================================================================

.. code-block:: javascript

    onWidgetClose() {}

Executed when a widget is removed from the grid. Make sure to clean up any resources in use by this widget. It is
not always necessary to override this function, but it's possible you're using a third party library that requires
action to be taken when the widget is removed. An example is the cleanup of a rendered chart.

-------
Styling
-------

Any styling can be added to the `Dashboard CSS file <https://github.com/opnsense/core/blob/master/src/opnsense/www/css/dashboard.css>`__

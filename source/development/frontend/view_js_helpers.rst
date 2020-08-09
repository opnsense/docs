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

----------
Guidelines
----------

.. rubric:: Some (simple) guidelines developing models
   :name: some-simple-guidelines-developing-models

#. One model should always be completely responsible for the its mount
   point, so if there's a model at mount point /A/B there can't be a
   model at /A/B/C
#. Try to keep models logical and understandable, it's better to build
   two models for you application if the content of two parts aren't
   related to each other. It's no issue to create models at deeper
   levels of the structure.

   #. When using more models in a application/module, you might want to
      consider the following naming convention: /Vendor/Module/Model

#. Try to avoid more disc i/o actions than necessary, only call save()
   if you actually want to save content, serializeToConfig just keeps
   the data in memory.

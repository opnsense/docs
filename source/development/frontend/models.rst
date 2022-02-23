===============
Creating Models
===============

A model represents the data which the application will use and takes
care of the interaction to that data. In OPNsense most of the relevant
data is physically stored in an XML structure (config.xml). The primary
goal for OPNsense models is to structure the use of configuration data,
by creating a clear abstraction layer.

In this chapter we will explain how models are designed and build.


.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   models_design
   models_example
   models_guidelines
   models_customfields
   models_constraints
   models_migrations

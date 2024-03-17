-------------------
Designing the model
-------------------

.. contents:: Index

Creating models for OPNsense is divided into two separate blocks:

#. A PHP class describing the actions on our data (also acts as a
   wrapper to our data),
#. The definition of the data and the rules it should apply to.

Every model's class should be derived from OPNsense\\Base\\BaseModel, a very
simple model without any (additional) logic is defined with:

.. code-block:: php

    <?php
    namespace myVendorName\myModule;
     
    use OPNsense\Base\BaseModel;
     
    class myModel extends BaseModel
    {
    }


This class should be placed inside the model directory of our project, in this
case the full path for our class file would be

-  /usr/local/opnsense/mvc/app/models/**myVendorName/myModule/myModel.php**

When you design a model, the next thing to do is to figure out what data is
relevant for your application or module and think of the rules it should comply
to (for example, if you need an email address you might want to validate the
input). Designing the actual model is as simple as creating an xml file and
putting in your structure, the name of our XML file should be the same as the
base name of our model suffixed by .xml.

Using the same model, we would create the following file:

-  /usr/local/opnsense/mvc/app/models/**myVendorName/myModule/myModel.xml**

And start describing our (information) model, like this:

.. code-block:: xml

    <model>
        <mount>//myManufacturer/myModule</mount>
        <description>A description of this model (metadata)</description>
        <version>1.0.0</version>
        <items>
            <exampleNumber type="TextField">
                <Mask>/^([0-9]){0,1}$/</Mask>
                <Default>5</Default>
                <ValidationMessage>you should input a number from 0 to 9</ValidationMessage>
            </exampleNumber>
            <contacts>
                <entity type="ArrayField">
                    <email type="EmailField">
                        <ValidationMessage>you should input a valid email address!</ValidationMessage>
                    </email>
                    <name type="TextField"/>
                </entity>
                <someText type="TextField"/>
            </contacts>
        </items>
    </model>

Now let's explain what's happing here one tag at a time.

#. the <model> tag is used for identification of the file. (this is a
   model file)
#. Next in line is the <mount> tag, this tells the system where this
   information lives in the configuration file, in this case
   ROOT\_tag/myManufacturer/myModule
#. If desired, there is some space reserved to explain the usage of the
   model, the <description> tag
#. A version tag is added, which is used to support migrations. These are described in more details in the :doc:`migration <models_migrations>` topic
#. Last item on the top of our list is the <items> tag, this is where
   the magic begins.

The content of a items tag describes the full tree based structure which holds
our data, in theory this could be as large as you want it to be, but keep in
mind that the content for your model should be logical and understandable. Every
node in the tree could have a type, which defines its behavior, nodes without a
type are just containers.

From top to bottom we find the following nodes in our tree:

-  exampleNumber, defined as a TextField

   -  Mask, validation can be performed by a regex expression, this sets
      the expression
   -  Default, this field is default filled with a number: 5
   -  ValidationMessage, when validation fails, this message is returned

-  contacts, this is a container
-  entity, is defined as a recurring item, which holds the next items
-  email, defined as an EmailField

   -  when validation fails, the **ValidationMessage** is returned

-  name, defined as a TextField without any validations
-  someText, not part of the entity tag and also defined as text without
   validation

The fieldtypes are easily extendable in the base system and all common ones live in
their own namespace at *OPNsense\\Base\\FieldTypes* deriving from *BaseField*.

.. Note::

   When designing application specific fieldtypes, you can point to a field
   type within the application namespace using a full or partial path.

   For example using *Vendor\\Component\\FieldTypes\\MyFieldType* to point to a specific non
   common field type or *.\\MyFieldType* when linked from the application model itself (which assumes a namespace FieldTypes
   exists)


volatile fields
.........................................

In some cases it can be practical to define fields which act as standard fields, but will not be persisted
in the configuration. Examples of this are fields used to generate other type of content, such as a certificate
or fields that reflect data stored elsewhere.

To make a field volatile, just add the tag :code:`volatile="true"` in the xml clause, for example:

::

   <serial type="IntegerField" volatile="true"/>



------------------------------------
Special model types
------------------------------------


In memory models
.........................................

In same cases it might be practical to use all of the standard model tools, but prevent data from being persisted.
For this purpose the memory model may be used. Examples of such applications are diagnostic tools, which do require
user input, but is only relevant for that perticular call.

To use these models, use the following mountpoint: :code:`<mount>:memory:</mount>`

Legacy wrappers
.........................................

While migrating legacy components, sometimes the distance between the current situation (using raw xml access) and the desired
one (being a fully validated model) is hard to overcome.
It's not always clear which type of data is being used, and when moving data inside a new model and changing it's access
path, a proper validation is mandatory.

When data lives inside it's own easy to distinct "container", a standard model may be overlayed. An example of such a
case is the static route component. Which underneath looks like this (without payload):


.. code-block:: xml

   <staticroutes>
      <route/>
      <route/>
   </staticroutes>


The other case is when a collection of items does not live inside a unique container,  for example the following
payload:


.. code-block:: xml

   <cert/>
   <cert/>
   <cert/>

Legacy modules would iterate over :code:`$config['cert']` in this case. Since :code:`cert` does not have an upper container
the model is able to control in full (as it's the root of the :code:`config.xml`), we can not overlay a standard model
to specify the fields used and their constraints.

This is where our legacy wrapper comes into play. In order to use this feature, you have to use the following mountpoint format:

   :code:`/tag+` << start with an exact path [:code:`/`] and end with a plus [:code:`+`]

In the "cert" example our mountpoint would like like : :code:`<mount>/cert+</mount>`

.. Note::

   All used fields still need to be specified, fields left out of the model, will be removed from the configuration
   in the same way a regular model would act.

.. Note::

   As legacy wrappers can not be versioned, migrations do not apply. In the long run
   it's always better to use full models, but these constructions offer an option for a "softer landing".

-------------------
Designing the model
-------------------

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

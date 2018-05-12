===============
Creating Models
===============

A model represents the data which the application will use and takes
care of the interaction to that data. In OPNsense most of the relevant
data is physically stored in an xml structure (config.xml). The primary
goal for OPNsense models is to structure the use of configuration data,
by creating a clear abstraction layer.

In this chapter we will explain how models are designed and build.

-------------------
Designing the model
-------------------

Creating models for OPNsense is divided into two separate blocks:

#. A php class describing the actions on our data (also acts as a
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
putting in your structure, the name of our xml file should be the same as the
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
node in the tree could have a type, which defines it's behavior, nodes without a
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


-------------
Usage example
-------------

Now let's test our model using a small php script (in /usr/local/opnsense/mvc/script/ ):

.. code-block:: php

    <?php
    // initialize phalcon components for our script
    require_once("load_phalcon.php");
     
    // include myModel and the shared config component
    use myVendorName\myModule\myModel;
    use OPNsense\Core\Config;
     
    // create a new model, reading the model definition and the current data from our config.xml
    $myMdl = new myModel();
    $myMdl->exampleNumber =1;
    $myMdl->contacts->someText = "just a test";
     
    // add a new contact node
    $node = $myMdl->contacts->entity->add();
    $node->email = "test@test.com";
    $node->name = "my test user";
     
    // perform validation on the data in our model
    $validationMessages = $myMdl->performValidation();
    foreach ($validationMessages as  $messsage) {
        echo "validation failure on field ". $messsage->getField()."  returning message : ". $messsage->getMessage()."\n";
    }
     
    // if validation succeeded, write data back to config
    if ($validationMessages->count() == 0) {
        // serialize our model to the config file (config.xml)
        // (this raises an error on validation failures)
        $myMdl->serializeToConfig();
        $cnf = Config::getInstance();
        $cnf->save();
    }


If you fill in an invalid value to one of the validated fields, you can easily
try the validation. Try to input the text "X" into the field exampleNumber to try out.

When inspecting our config.xml file, you will notice the following content has
been added to the root:

.. code-block:: xml

      <myManufacturer>
        <myModule>
          <exampleNumber>1</exampleNumber>
          <contacts>
            <entity>
              <email>test@test.com</email>
              <name>my test user</name>
            </entity>
            <someText>just a test</someText>
          </contacts>
        </myModule>
      </myManufacturer>

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

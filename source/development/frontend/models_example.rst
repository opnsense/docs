-------------
Usage example
-------------

Now let's test our model using a small PHP script (in /usr/local/opnsense/mvc/script/ ):

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

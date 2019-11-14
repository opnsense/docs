-----------------------------------
Custom (app specific) field types
-----------------------------------

Applications can add their own custom field types, which should be derived from :code:`BaseField` or one of its descendants.
A very simple single item custom field type could look like this:

Build the field type
........................................

.. code-block:: php

    <?php
    namespace myVendorName\myModule;
    use OPNsense\Base\FieldTypes\BaseField;
    use Phalcon\Validation\Validator\Regex;
     
    class SimpleCustomField extends BaseField
    {
        protected $internalIsContainer = false;
        protected $internalValidationMessage = "standard error";
        public function getValidators()
        {
            $validators = parent::getValidators();
            $reservedwords = array('all', 'pass', 'block', 'out');
            $validators[] = new ExclusionIn(array(
                'message' => 'can not use a reserved word',
                'domain' => $reservedwords));
        }
        return $validators;
    }

This example extends the standard validations with a list of reserved words, in which case it would yield :code:`can not use a reserved word`
if one of the reserved words are provided.

.. Note::

    This file should be placed in the subdirectory :code:`FieldTypes` of the model itself.

.. Tip::

    Use :code:`BaseListField` as simple template for list type items.


Use in model
.................

The validation can be used as any standard type, when prefixed with :code:`.\ ` the model knows it concerns a local field.

.. code-block:: xml

    <model>
        <mount>//OPNsense/MyFirst/App</mount>
        <version>1.0.0</version>
        <description>
            My first application
        </description>
        <items>
            <general>
                <name type=".\SimpleCustomField">
                    <Required>Y</Required>
                </name>
            </general>
        </items>
    </model>


.. Tip::

    Inspect the `basic field <https://github.com/opnsense/core/tree/master/src/opnsense/mvc/app/models/OPNsense/Base/FieldTypes>`__ types
    for inspiration, a concrete example of a custom field type can be found in the
    `firewall <https://github.com/opnsense/core/tree/master/src/opnsense/mvc/app/models/OPNsense/Firewall>`__ section

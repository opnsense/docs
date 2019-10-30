=================
Model Constraints
=================


-------------------------
ComparedToFieldConstraint
-------------------------

The CoparedToFieldConstraint copares the value of the current field to the value of a referenced field
on the same level (for example in the same ArrayField).
It is for example used for the rspamd_ plugin, to ensure that some values are in the correct order.
This constraint can be used to compare numeric values.

.. _rspamd: https://github.com/opnsense/plugins/blob/master/mail/rspamd/src/opnsense/mvc/app/models/OPNsense/Rspamd/RSpamd.xml

Example:

::

    <check003>
      <ValidationMessage>This field must be bigger than the greylist score.</ValidationMessage>
      <type>ComparedToFieldConstraint</type>
      <field>greylistscore</field>
      <operator>gt</operator>
    </check003>

In this example, the valueof the current field must be greater than the value of the field "greylistscore".

Field values:

================= ====================================================================================
ValidationMessage Validation message (translateable) which will be shown in case the validation fails.
type              ComparedToFieldConstraint
field             the other field which we reference
operator          The operator to check the value. Valid operators are gt, gte, lt, lte, eq, neq
================= ====================================================================================

Operators:

=== =====================
gt  greater than
gte greater than or equal
lt  lesser than
lte lesser than or equal
eq  equal
neq not equal
=== =====================



---------------
SetIfConstraint
---------------

The SetIfConstraint is used to make some fields conditionally mandatory. It is mainly used in the nginx_
plugin for example to choose an implementation type. In general the other field should be an OptionField,
but does not need to. In general it is a good idea to hide or show fields which are (not)
required by an implementation in the frontend as well to simplify the web interface.
Please note: the checked field is intended to be on the same level (for example ArrayField).

.. _nginx: https://github.com/opnsense/plugins/blob/master/www/nginx/src/opnsense/mvc/app/models/OPNsense/Nginx/Nginx.xml

Example:

::

    <check001>
      <ValidationMessage>This field must be set.</ValidationMessage>
      <type>SetIfConstraint</type>
      <field>match_type</field>
      <check>id</check>
    </check001>

In this example, the value will be mandatory, if the field "match_type" has the value "id".

Field Values:

================= ====================================================================================
ValidationMessage Validation message (translateable) which will be shown in case the validation fails.
type              SetIfConstraint
field             the other field which we reference
check             The value of the other field which makes this field required
================= ====================================================================================


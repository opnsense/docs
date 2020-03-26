-------------------
Migrations
-------------------

When using the :code:`<version/>` tag in the model xml you automatically allow upgrades of your configuration data. If the
tag is missing, it will automatically assume your at version :code:`0.0.0` (initial version).

The migration feature provides a pluggable framework to offer new and changed attributes after installation of new software and
is therefor automatically triggered when performing upgrades or installing packages.


.. Tip::
    You can always trigger migrations manually by executing :code:`/usr/local/opnsense/mvc/script/run_migrations.php` from
    a console. This will output all installed modules and the upgrades performed.


If no overrides are provided and the module version of the running configuration doesn't equal the one installed,
there automatically will be a migration created using the :code:`BaseModelMigration` base class.
This will take care of basic changes, such as adding new fields and applying defaults.

.. Note::

  The current version will always be saved as an attirbute on the model xml (e.g. :code:`<Alias version="1.0.0">`)


.............................
Custom migrations
.............................

In some cases one wants to perform custom actions when upgrading between version, such as gathering data from legacy
configuration settings.


The directory :code:`Migrations` in the model directory is used to hold the migration code on a per version basis.
By default classes (and files) in there use the following naming scheme: :code:`M1_0_0` which stands for [M]igration version
[1.0.0].

.. Note::
    If different models share a namespace, you can change the prefix of the migration files, when nothing is provided
    the default is **M**, the tag :code:`<migration_prefix/>` can be used to change this to something else. (e.g. :code:`<migration_prefix>MFP</migration_prefix>`)

The boilerplate for a model migration looks like this (for a migration to 1.0.0):

.. code-block:: php

    class M1_0_0 extends BaseModelMigration
    {
        /**
         * default model migration
         * @param $model
         */
        public function run($model)
        {
            parent::run($model);
        }

        /**
         * post migration action, run after config sync
         * @param $model
         */
        public function post($model)
        {
            return;
        }
    }


It contains two methods, :code:`run()` and :code:`post()`. The first one is executed in memory, before serializing data
back to the running configuration and for all version steps in sequence. (an upgrade from 1.0.0 to 1.0.2 might execute 1.0.1, 1.0.2, 1.0.3).
The configuration data itself will be synced ones in this case.


The post action is called after normal model configuration and can sometimes be practical to alter the raw model xml, for example if
model versions require a move of datasets, without actually changing content.


.. Note::

  Although there are toggles in place, data migration can easily lead to race conditions. Always try to design your software for change,
  adding fields which pass validation by default for example is always preferred above situations which will fail by default.

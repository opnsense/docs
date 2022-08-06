===============
Using Templates
===============

-------
General
-------

For config file generation, we provide a backend service which can bind
config.xml data to templates written in Jinja2
(http://jinja.pocoo.org/docs/dev/).

All available templates should be installed at the following location on
the OPNsense system:

#. /usr/local/opnsense/service/templates/


-----------------
Naming convention
-----------------

All templates should be put into a directory structure containing the
vendor and package/application name, our sample application is placed
inside the directory:

/usr/local/opnsense/service/templates/*OPNsense/Sample*

Template package content

Every template directory should contain at least 2 files:

#. a content descriptor, containing the actual targets, named +TARGETS
#. one or more template(s)


-------
Targets
-------

The +TARGETS file contains the source template name inside the template
directory and the (dynamic) target filename divided by a colon (:)
multiple lines may be inserted per file.

For example :

::

    example_simple_page.txt:/tmp/template_sample/simple_page.txt

Will create a file /tmp/template\_sample/simple\_page.txt using the
template example\_simple\_page.txt.

.. Note::

    Optionally you can specify which file or files to remove on call of "template cleanup", which can be specified by
    using an extra tag next to the target, such as:
    :code:`example_simple_page.txt:/tmp/template_sample/simple_page.txt:/tmp/template_sample/simple_page.*`

    By default all targets will be removed when calling cleanup.



If you want to use information from within the config.xml file as output
filename, you can use tags to address the content, like [version] to
input the tag version from the xml file. When generating multiple files
from 1 template, you can use one wildcard (%) to address a section of
the config file, for example [interfaces.%.if] loops over the interfaces
and outputs the value of **if**.

-----------------
Target overwrites
-----------------

Every template package can specify overwrites, which can be used by vendors who implement and maintain their own templates
for features in OPNsense.

Simply add files using the target definition in the **+TARGETS.D** directory of the templates folder using as extension **.TARGET**.

For example an overwrite for OPNsense/Sample can use the following name and location
:code:`/usr/local/opnsense/service/templates/OPNsense/Sample/+TARGETS.D/custom.TARGET`

.. Note::
    Be vey careful using this feature, you need to maintain these templates yourself and features may break after upgrades
    of OPNsense.

---------
Templates
---------

For more information of the template language itself, please look at
http://jinja.pocoo.org/docs/dev/ and the examples installed in
/usr/local/opnsense/service/templates/OPNsense/Sample.

There's one special case when using the template engine, every wildcard
used for the output file generation is also provided to the template, so
you are able to determine which filter let to this output.

Those filters are stored in the variable TARGET\_FILTERS.

.. code-block:: jinja

        {% if TARGET_FILTERS['interfaces.wan'] %}
        {% endif %}

----------
Test usage
----------

The templates can be rendered via the backend service (configd), to test
this functionality on a running OPNsense system, use:


::

    # generate template package
    configctl template reload OPNsense/Sample
    # cleanup files
    configctl template cleanup OPNsense/Sample

|

-----------------------------
Python template usage example
-----------------------------

The template system itself is a separate module which is used by
configd, to use (or test) the system without the daemon, use:

.. code-block:: python

    # import template system and config.xml handling
    from modules import template
    from modules import config
     
    # construct a new template object, set root to /tmp/
    tmpl = template.Template(target_root_directory='/tmp/')
    # open the config.xml and bind to template object
    conf = config.Config('/config.xml')
    tmpl.set_config(conf.get())
     
    # generate output for OPNsense/Sample
    generated_filenames = tmpl.generate('OPNsense/Sample')
     
    # print results
    for filename in generated_filenames:
      print ('.. generated : %s'%filename)

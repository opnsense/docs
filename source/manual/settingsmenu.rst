=============
Settings menu
=============

Besides the configuration options that every component has, OPNsense also contains a lot of general settings
that you can tweak. This page contains an overview of them.

--------
Tunables
--------

Tunables are the settings that go into the ``sysctl.conf`` file, which allows tweaking of low-level system
settings. They can be set by going to :menuselection:`System --> Settings --> Tunables`.

Here, the currently active settings can be viewed and new ones can be created. All valid ``sysctl.conf``
settings can be added this way if desired. A list of possible values can be obtained by issuing
``sysctl -a`` on an OPNsense shell.
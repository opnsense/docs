======
ntopng
======

------------
Installation
------------

First of all, you have to install the ntopng plugin (os-ntopng) from the plugins view
reachable via :menuselection:`System --> Firmware --> Plugins`.

After a page reload you will get a new menu entry under **Services** for ntopng. If you
don't have Redis plugin installed, you'll receive a warning in ntopng main menu. Please
go back to :menuselection:`System --> Firmware --> Plugins`, install os-redis, change to :menuselection:`Services --> Redis`
and just enable the service. That's enough to run ntopng.

----------------
General Settings
----------------

:Enable ntopng:
    Enable and start ntopng.
:Interfaces:
    Here you set the interfaces ntopng should listen on. If you don't select any interface
    it listens to the first in the system, e.g. em0, but you can change the interfaces 
    within ntopng's UI on demand; while setting an explicit interface you wont get any 
    other interface presented in its own UI.
:HTTP Port:
    The port ntopng's UI should listen on. When you leave it on the default just open a 
    browser and go to your Firewall IP with port 3000 and HTTP. If you want to secure the 
    connection feel free to setup HAProxy or Nginx as a reverse proxy (SSL offloading).
:DNS Mode:
    Here you can choose if ntopng should try to resolve IPs to host names.

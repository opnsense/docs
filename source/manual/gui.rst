===========================
The OPNsense User Interface
===========================

This article explains the basics of the OPNsense Graphical User Interface or GUI
for short.

----------
User Login
----------
Before we can take a look at the GUI options we need to login.
The default user is root and the password is opnsense.

.. image:: images/login.png


----------------------------
GUI Layout & Main Components
----------------------------

The GUI consists out of the following main components:

.. image:: images/gui_layout.png
  :width: 100%


Logo & Link to Lobby
---------------------
Click on the OPNsense logo wherever you are in the interface and you will be
directed to the lobby and dashboard.

In the Lobby you can:

* Look at the dashboard with widgets
* View the 2 clause BSD license
* Change your password
* Logout

Menu Area
---------
The Menu area holds all the primary and sub menu's.
Here you can select what part of the system you want to watch or change.

You can see the layering on the menu. There are three levels:

#. Category level
#. Function level
#. Configuration level *(may not exist if the function is simple)*

In the following sample you see a screenshot of the Category **System**, with:

* Function: **Settings**
* Selected Configuration item: **General**

.. image:: images/submenu.png

Quick Navigation
----------------
A faster way to navigate trough the gui is by using the quick navigation/search box
on the upper right corner of the screen. Either click on it or hit tab to select it.

The search field is a type-a-head field, meaning that it will guess what you are
looking for and fill up while typing. Hit enter or click on an option to select
and navigate directly to the right page.

.. image:: images/quick-navigation.png


User & Local domain
-------------------
In the right corner just to the left of the quick navigation you will see your
username and the full domain name the firewall is configured with
(to change firewall name, go to **System->Setting->General**).


Content Area
------------
The content area is used to display:

* Input forms
* Popup Forms
* Buttons
* General forms of data output graphical and text based

----------
Form View
----------
Lets take a look at how an advanced form may look like:

.. image:: images/proxy_form.png

Full Help
---------
Many Forms are equipped with build-in help. In the upper right corner of the form
you can select to view all help messages at once. The toggle will color green when
enabled and show the help messages beneath the input items.

.. image:: images/help_msg.png


Advanced Mode
-------------
Some forms have hidden advanced features, to view them toggle the **advanced mode** in
the left corner of the form. Doing so will reveal all advanced options.

.. image:: images/advanced.png


Single Item Help
----------------
Show a single line help by pressing the **(i)** left of a form item.
Like this:

.. image:: images/info.png


Standard Tabs
-------------
A standard tab can be clicked upon to open the corresponding form.

A sample can be seen here:

.. image:: images/tab.png

Dropdown Tabs
-------------
A dropdown tab can be clicked upon to open the first menu item or you can click on
the arrow next to it to show all options, like:

.. image:: images/dropdown_tab.png

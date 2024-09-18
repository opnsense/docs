=========
Dashboard
=========

The Dashboard is the first page you will see after you log into OPNsense.
Additionally, it can be accessed via :menuselection:`Lobby --> Dashboard`.
The Dashboard provides an overview of your system status.

-------------
Configuration
-------------

What is shown on the Dashboard can be configured by adding and removing widgets.
Some widgets also allow further configuration.

By default, the following widgets are present:

* **System Information**  Shows information about the installed OPNsense version, updates etc.
* **Memory** Shows memory usage.
* **Disk** Shows disk usage.
* **CPU** Shows CPU usage.
* **Announcements** Shows the latest announcements from the OPNsense project.
* **Gateways** Shows used gateways.
* **Interface Statistics** Shows the number of packets, bytes and errors handled by each interface.
* **Firewall** Collects logged events from the moment the dashboard has loaded to represent a snapshot of what the firewall is currently seeing. Can be expanded to show a live log.
* **Traffic Graph** Shows traffic passing through the system.
* **Services** Shows the configured services as well as the options to start/restart/stop them.

In the upper right corner of the page, you can find the following buttons:

* **Edit dashboard (pencil icon)** Enter edit mode. Unlocks the dashboard temporarily so you can move, resize, remove, or configure widgets.
* **Add widget (plus icon)** Opens a dialog window with a list of widgets that can be added to the Dashboard. Simply click on an entry in the list to add it to the Dashboard.
* **Restore default layout (widgets icon)**  Restores the dashboard to its default configuration discarding all your modifications.
* **Save** After editing the dashboard, you can make all changes persistent by clicking this button. Otherwise the changes will be discarded as soon as you reload the page.

If the dashboard is in edit mode, the following buttons are available in the upper right corner of every widget:

* **Edit (pencil icon)** Click this to modify the widget settings. This button is only present if the widget is configurable.
* **Remove (cross icon)** Removes the widget from the Dashboard.

If the widget is not in edit mode, you can find a link in the upper right corner of each widget if applicable, which will take you to the relevant configuration page.

All widgets can be resized by dragging on one of the corners of the widget.

.. Note::

    The dashboard configuration is saved per user. This means that each user can have their own dashboard layout.
    Therefore, use the "Users and Groups" high availability option to synchronize the dashboard configuration.

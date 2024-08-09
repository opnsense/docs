=========
Dashboard
=========

The Dashboard is the first page you will see after you log into OPNsense.
Additionally, it can be accessed via :menuselection:`Lobby --> Dashboard`. The Dashboard provides an overview of your system status.

-------------
Configuration
-------------

What is shown on the Dashboard can be configured by adding and removing widgets. Some widgets also allow further
configuration.

By default, the following widgets are present:

* **System Information:**  Shows information about the installed OPNsense version, updates etc.
* **Memory** Shows memory usage.
* **Disk** Shows disk usage.
* **CPU** Shows CPU usage.
* **Announcements** Shows the latest announcements from the OPNsense project.
* **Gateways:** Shows used gateways.
* **Interface Statistics** Shows the number of packets, bytes and errors handled by each interface.
* **Firewall** Collects logged events from the moment the dashboard has loaded to represent a snapshot of what the firewall is currently seeing. Can be expanded to show a live log.
* **Traffic Graph** Shows traffic passing through the system.

In the upper right corner of every widget, there can be two buttons:

* **Edit (pencil icon):** Click this to modify the widget settings. This button is only present if the widget is configurable.
* **Remove (cross icon):** Removes the widget from the Dashboard.

In the upper right corner of the page, there are two or three buttons:

* **Add widget:** Opens a dialog window with a list of widgets that can be added to the Dashboard. Simply click on an entry in the list to add it to the Dashboard.
* **Save Settings:** When you change the amount of columns or collapse a widget, you can make that change persistent by clicking this button. Otherwise the changes will be discarded as soon as you reload the page.
* **Lock** Locks the dashboard so you cannot move, remove or resize widgets. New widgets can still be added. This change is persisted and is useful to navigate the dashboard on a mobile device.

All widgets can be resized by dragging on one of the corners of the widget. The widget will snap to the grid, so it will always fit in the available space.

.. Note::

    The dashboard configuration is saved per user. This means that each user can have their own dashboard layout.

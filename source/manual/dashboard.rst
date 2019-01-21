=========
Dashboard
=========

The Dashboard is the first page you will see after you log into OPNsense.
Additionally, it can be accessed via **Lobby->Dashboard**. The Dashboard provides an overview of your system status.

-------------
Configuration
-------------

What is shown on the Dashboard can be configured by adding and removing widgets. Some widgets also allow further
configuration.

By default, the following widgets are present:

* **System Information:**  Shows information about the installation OPNsense version, the hardware in the computer and resource usage.
* **Services:** Shows running background services and allow starting, stopping and reloading them.
* **Gateways:** Shows used gateways.
* **Interfaces:** Shows configured interfaces and their status.

In the upper right corner of every widget, there are three buttons:

* **Edit (pencil icon):** Click this to modify the widget settings. This button is always present, but it can be greyed out if the widget has no configuration options.
* **Minimize (minus icon):** Click this to temporarily collapse this widget. It can be uncollapsed by clicking the 'plus' icon.
* **Remove (cross icon):** Removes the widget from the Dashboard.

In the upper right corner of the page, there are two or three buttons:

* **Add widget:** Opens a dialog window with a list of widgets that can be added to the Dashboard. Simply click on an entry in the list to add it to the Dashboard.
* **1/2/3/4/6 columns:** Changes the amount of columns to show widgets in. By default, this is set to **2**. Do not forget to click **Save Settings** afterwards.
* **Save Settings:** When you change the amount of columns or collapse a widget, you can make that change persistent by clicking this button. Otherwise the changes will be discarded as soon as you reload the page.
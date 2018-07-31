===========================
Configuring Cellular Modems
===========================
OPNsense supports a wide range of USB and miniPCIe cellular modems that can be used
as primary internet (WAN) connection or as failover for a fixed/ethernet connection.

With this guide we show you how to easily add a new modem and configure it to be
used as primary WAN connection.

----------------------------
Devices used for this How-to
----------------------------
For this how-to we used a `Deciso Netboard A10 desktop appliance <https://www.deciso.com/product-catalog/opn20076b/>`__
and a Huawei ME909u-521 miniPCIe cellular modem provided by `OSNet <https://www.osnet.eu/>`__.

.. Note::
   Support for the ME909u-521 will be added in OPNsense 16.1.18.

----------------------------------------
Step 1 - Configure Point to Point device
----------------------------------------
Go to **Interfaces->Point-to-Point->Devices** and click on **Add** in the upper
right corner of the form.

Fill in the form like this (Example is for Dutch Mobile 4G KPN Subscription):

============================ =======================================================
 **Link Type**                PPP
 **Link interface(s)**        /dev/cuaU0.0 ( HUAWEI Mobile Connect - Modem)
 **Description**              4G Cellular Network
 **Service Provider**         Select Country, Provider & Plan for auto configuration
 **Username**                 Leave Empty (for NL KPN)
 **Password**                 Leave Empty (for NL KPN)
 **Phone Number**             \*99# (for NL KPN)
 **Access Point Name (APN)**  fastinternet (for NL KPN 4G)
============================ =======================================================

If you need to enter a PIN number then click on **Advanced Options**

Click **Save** to apply the settings.

.. image:: images/4g_configure_ppp.png
   :width: 100%


.. image:: images/ppp_celular_configured.png
   :width: 100%

---------------------------------
Step 2 - Assign the WAN interface
---------------------------------
To assign the interface go to **Interfaces->Assignments** in our case we will make
this our primary internet connection and change the WAN assignment accordingly.

To do so just change the **Network port** for **WAN** to **ppp0 (/dev/cuaU0.0) - 4G Cellular Network**.

No click **Save** below the form.

If everything went fine then your are all setup and the default gateway will be
the one of you cellular connection.

.. image:: images/Interface_assignment_4g.png
   :width: 100%

-------------------------
Step 3 - Trouble shooting
-------------------------
Ok, so it doesn't work as expected.
In that case, first look at the log of the cellular device's PPP connection, to do
so go to: **Interfaces->Point-to-Point->Log File**. Often you can see what went
wrong directly in the log.

If you can't figure out what is wrong then a reboot to reinitialize the device can
sometimes help.

.. Note::

  Before booting your device it is best to make sure the SIM card is inserted correctly.


When the device seems to work properly then checkout if the interface was assigned
an IP address, go to **Interfaces->Overview** and click on the WAN interface to
see the details.

You should see an IP address, Gateway IP and ISP DNS server(s).
If all is filled in then either your firewall is blocking the traffic or the
network connection is not working well.

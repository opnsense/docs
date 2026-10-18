Setup for Sky UK ISP
====================

**Original Author:** Martin Wasley

**Introduction**
-----------------
This doc covers the setup of OPNsense on a Sky UK VDSL connection.

Sky uses a simple IPoE connection, all that is required is a suitable modem
in bridge mode. If using a standard OpenReach modem then no setting is required
in the modem itself.

**WAN Interface**
-----------------

Go to :menuselection:`Interfaces --> Assignments` and edit WAN.

Set both IPv4 and IPv6 configuration type to DHCP and DHCPv6 respectively.

**Option61 - dhcp-client-identifier**
-------------------------------------

We now need to send the Sky login credentials. When using VDSL we do not
need to use specific credentials, as long as they are correctly formatted
anything will do.

Enable advanced mode in the interface dialog to show **Send Options**.

Enter the client identifier as hexadecimal bytes in **Send Options**. For the
example credentials below, use:

``dhcp-client-identifier 31:32:33:34:35:36:37:38:40:73:6b:79:64:73:6c:7c:31:32:33:34:35:36:37:38``

It is said that it doesn't matter what is sent in the option61 string, which
is what this is, as long as something is sent, I prefer to play it safe so
stick with the format as shown. For example, the following will work quite
happily.

dhcp-client-identifier "12345678@skydsl|12345678"

The other part of the ID is called Option60, there are varying thoughts on
whether this is needed anymore, it does no harm to include it so we'll do so.

Use ``\174`` as the octal escape for the pipe in the class identifier because the validated option field does not
accept a literal pipe.

Add each option on its own line. The full **Send Options** value is therefore::

    dhcp-client-identifier 31:32:33:34:35:36:37:38:40:73:6b:79:64:73:6c:7c:31:32:33:34:35:36:37:38
    dhcp-class-identifier "7.16a4N_UNI\174PCBAFAST2504Nv1.0"



The next step is to configure the parameters required for DHCPv6 in the WAN
interface's IPv6 address configuration fields.

Sky provide a /56 IPv6 delegation, they do not provide a global IPv6 address
on the WAN interface, this is link local only. Prefix delegation size should
be set to 56.

Click 'Save' and 'Apply'

The only other requirement is found in the Interfaces:Settings menu under
IPV6 DHCP. The ‘Prevent Release' option.

.. image:: images/skyuk_dhcp6c_interface_settings.png
	:width: 100%

This is there as the Sky DHCPv6 servers use a 'sticky' address. If the
OPNsense dhcp6 client sends a release signal to the server it's more than
likely that the allocated prefix will change, thus this setting, along with
the 'DHCP Unique Identifier' setting will attempt to mitigate this risk.

Once these settings have been entered, click on 'Save' then 'Apply'.

**DHCP Unique Identifier**
--------------------------

Although OPNsense stores the IPv6 DUID it is possible this can be lost, this
again would probably result in a new prefix being given, therefore an option
to enter and store a DUID is given in the Interface:Settings menu.

.. image:: images/skyuk_wan_3.png
	:width: 100%

The Identifier can either be entered manually or if the user clicks on the 'i'
icon, the existing DUID can be automatically entered into the field by clicking
on the 'Insert the existing DUID here' legend.

Click ‘Save’.

**LAN Interface**
-----------------
The LAN interface IPv4 address should have been set up during initial system
installation. If it was not, edit LAN under :menuselection:`Interfaces --> Assignments`.

It is my recommendation not to use the private subnet range 192.168.*.0, as
this range is often used by hotels and other public networks for access, this
can cause issues when using a VPN. My preferred address method is using the
10.*.*.0 subnet where the second and third quartet are birth dates or some
other easily memorable number. i.e. 10.1.11.0 would be the first of November.
This is more random and the chances of the same range on a public network is
greatly reduced, however the address range is easily memorable.

Once the LAN IPv4 address is set then all that remains in the LAN interface
is to set the interface to use the assigned IPv6 prefix.

Set **IPv6 Configuration Type** to **Track Interface (legacy)**, choose WAN as the
**Parent interface** and set **Assign prefix ID** to ``0x0`` unless you have a special requirement.

Click ‘Save’ and then ‘Apply’.

Setting up the IPv4 DHCP server is not covered in this document, but is
required.

It is advisable at this point to reboot the system.

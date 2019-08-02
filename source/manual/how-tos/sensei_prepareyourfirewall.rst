===============================
Sensei: Prepare Your Firewall
===============================

.. Note::

    To install Sensei on your OPNsense firewall, you need to connect to it via ``ssh`` with ``root`` privileges.

-----------------------------

---------------------
Enable Secure Shell
---------------------

1. Login to your OPNsense firewall's dashboard
2. Head to the :menuselection:`System > Settings > Administrations` menu
3. Enable all three checkboxes

   1. Enable Secure Shell
   2. Permit root user login
   3. Permit password login

.. image:: images/sensei/opnsense-admin-secure-shell-settings.png
    :width: 100%

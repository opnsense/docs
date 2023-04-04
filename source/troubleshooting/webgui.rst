====================================
WebGui access reset
====================================

If for some reason the webgui certificate is broken, you can reconfigure access using the console menu.
Select :code:`Set interface IP address` (option 2) from the menu, reconfigure an interface, after providing the
address configuration you can either (temporary) switch back to :code:`HTTP` or in the next step generate a new self-signed certificate.

It is also possible to reset the defaults in the final step ("**Restore web GUI access defaults?**"),
in case something went wrong while setting up anti lockout policies or after changing interfaces.


.. Tip::
    When logged in directly via a console or shell, you can also use the following command to generate a new self-signed certificate
    and restart the web ui:

    :code:`configctl webgui restart renew``



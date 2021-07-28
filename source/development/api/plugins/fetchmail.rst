Fetchmail
~~~~~~~~~

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","fetchmail","general","get",""
    "``GET``","fetchmail","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/mail/fetchmail/src/opnsense/mvc/app/models/OPNsense/Fetchmail/General.xml>`__"

.. csv-table:: Resources (MailboxController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","fetchmail","mailbox","addMailbox",""
    "``POST``","fetchmail","mailbox","delMailbox","$uuid"
    "``GET``","fetchmail","mailbox","get",""
    "``GET``","fetchmail","mailbox","getMailbox","$uuid=null"
    "``*``","fetchmail","mailbox","searchMailbox",""
    "``GET``","fetchmail","mailbox","set",""
    "``POST``","fetchmail","mailbox","setMailbox","$uuid"
    "``POST``","fetchmail","mailbox","toggleMailbox","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Mailbox.xml <https://github.com/opnsense/plugins/blob/master/mail/fetchmail/src/opnsense/mvc/app/models/OPNsense/Fetchmail/Mailbox.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","fetchmail","service","reconfigure",""
    "``GET``","fetchmail","service","restart",""
    "``GET``","fetchmail","service","start",""
    "``GET``","fetchmail","service","status",""
    "``GET``","fetchmail","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/mail/fetchmail/src/opnsense/mvc/app/models/OPNsense/Fetchmail/General.xml>`__"

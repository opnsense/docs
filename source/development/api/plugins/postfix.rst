Postfix
~~~~~~~

.. csv-table:: Resources (AddressController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","address","addAddress",""
    "``POST``","postfix","address","delAddress","$uuid"
    "``GET``","postfix","address","get",""
    "``GET``","postfix","address","getAddress","$uuid=null"
    "``*``","postfix","address","searchAddress",""
    "``GET``","postfix","address","set",""
    "``POST``","postfix","address","setAddress","$uuid"
    "``POST``","postfix","address","toggleAddress","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Address.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Address.xml>`__"

.. csv-table:: Service (AntispamController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","postfix","antispam","get",""
    "``GET``","postfix","antispam","set",""

    "``<<uses>>``", "", "", "", "*model* `Antispam.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Antispam.xml>`__"

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","domain","addDomain",""
    "``POST``","postfix","domain","delDomain","$uuid"
    "``GET``","postfix","domain","get",""
    "``GET``","postfix","domain","getDomain","$uuid=null"
    "``*``","postfix","domain","searchDomain",""
    "``GET``","postfix","domain","set",""
    "``POST``","postfix","domain","setDomain","$uuid"
    "``POST``","postfix","domain","toggleDomain","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Domain.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Domain.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","postfix","general","get",""
    "``GET``","postfix","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/General.xml>`__"

.. csv-table:: Resources (HeaderchecksController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","headerchecks","addHeadercheck",""
    "``POST``","postfix","headerchecks","delHeadercheck","$uuid"
    "``GET``","postfix","headerchecks","get",""
    "``GET``","postfix","headerchecks","getHeadercheck","$uuid=null"
    "``*``","postfix","headerchecks","searchHeaderchecks",""
    "``GET``","postfix","headerchecks","set",""
    "``POST``","postfix","headerchecks","setHeadercheck","$uuid"
    "``POST``","postfix","headerchecks","toggleHeadercheck","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Headerchecks.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Headerchecks.xml>`__"

.. csv-table:: Resources (RecipientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","recipient","addRecipient",""
    "``POST``","postfix","recipient","delRecipient","$uuid"
    "``GET``","postfix","recipient","get",""
    "``GET``","postfix","recipient","getRecipient","$uuid=null"
    "``*``","postfix","recipient","searchRecipient",""
    "``GET``","postfix","recipient","set",""
    "``POST``","postfix","recipient","setRecipient","$uuid"
    "``POST``","postfix","recipient","toggleRecipient","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Recipient.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Recipient.xml>`__"

.. csv-table:: Resources (RecipientbccController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","recipientbcc","addRecipientbcc",""
    "``POST``","postfix","recipientbcc","delRecipientbcc","$uuid"
    "``GET``","postfix","recipientbcc","get",""
    "``GET``","postfix","recipientbcc","getRecipientbcc","$uuid=null"
    "``*``","postfix","recipientbcc","searchRecipientbcc",""
    "``GET``","postfix","recipientbcc","set",""
    "``POST``","postfix","recipientbcc","setRecipientbcc","$uuid"
    "``POST``","postfix","recipientbcc","toggleRecipientbcc","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Recipientbcc.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Recipientbcc.xml>`__"

.. csv-table:: Resources (SenderController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","sender","addSender",""
    "``POST``","postfix","sender","delSender","$uuid"
    "``GET``","postfix","sender","get",""
    "``GET``","postfix","sender","getSender","$uuid=null"
    "``*``","postfix","sender","searchSender",""
    "``GET``","postfix","sender","set",""
    "``POST``","postfix","sender","setSender","$uuid"
    "``POST``","postfix","sender","toggleSender","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Sender.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Sender.xml>`__"

.. csv-table:: Resources (SenderbccController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","senderbcc","addSenderbcc",""
    "``POST``","postfix","senderbcc","delSenderbcc","$uuid"
    "``GET``","postfix","senderbcc","get",""
    "``GET``","postfix","senderbcc","getSenderbcc","$uuid=null"
    "``*``","postfix","senderbcc","searchSenderbcc",""
    "``GET``","postfix","senderbcc","set",""
    "``POST``","postfix","senderbcc","setSenderbcc","$uuid"
    "``POST``","postfix","senderbcc","toggleSenderbcc","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Senderbcc.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Senderbcc.xml>`__"

.. csv-table:: Resources (SendercanonicalController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","sendercanonical","addSendercanonical",""
    "``POST``","postfix","sendercanonical","delSendercanonical","$uuid"
    "``GET``","postfix","sendercanonical","get",""
    "``GET``","postfix","sendercanonical","getSendercanonical","$uuid=null"
    "``*``","postfix","sendercanonical","searchSendercanonical",""
    "``GET``","postfix","sendercanonical","set",""
    "``POST``","postfix","sendercanonical","setSendercanonical","$uuid"
    "``POST``","postfix","sendercanonical","toggleSendercanonical","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Sendercanonical.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Sendercanonical.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","postfix","service","checkrspamd",""
    "``POST``","postfix","service","reconfigure",""
    "``GET``","postfix","service","reconfigure",""
    "``GET``","postfix","service","restart",""
    "``GET``","postfix","service","start",""
    "``GET``","postfix","service","status",""
    "``GET``","postfix","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/General.xml>`__"

Postfix
~~~~~~~

.. csv-table:: Resources (AddressController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","address","add_address",""
    "``POST``","postfix","address","del_address","$uuid"
    "``GET``","postfix","address","get",""
    "``GET``","postfix","address","get_address","$uuid=null"
    "``*``","postfix","address","search_address",""
    "``POST``","postfix","address","set",""
    "``POST``","postfix","address","set_address","$uuid"
    "``POST``","postfix","address","toggle_address","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Address.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Address.xml>`__"

.. csv-table:: Service (AntispamController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","postfix","antispam","get",""
    "``POST``","postfix","antispam","set",""

    "``<<uses>>``", "", "", "", "*model* `Antispam.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Antispam.xml>`__"

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","domain","add_domain",""
    "``POST``","postfix","domain","del_domain","$uuid"
    "``GET``","postfix","domain","get",""
    "``GET``","postfix","domain","get_domain","$uuid=null"
    "``*``","postfix","domain","search_domain",""
    "``POST``","postfix","domain","set",""
    "``POST``","postfix","domain","set_domain","$uuid"
    "``POST``","postfix","domain","toggle_domain","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Domain.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Domain.xml>`__"

.. csv-table:: Service (GeneralController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","postfix","general","get",""
    "``POST``","postfix","general","set",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/General.xml>`__"

.. csv-table:: Resources (HeaderchecksController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","headerchecks","add_headercheck",""
    "``POST``","postfix","headerchecks","del_headercheck","$uuid"
    "``GET``","postfix","headerchecks","get",""
    "``GET``","postfix","headerchecks","get_headercheck","$uuid=null"
    "``*``","postfix","headerchecks","search_headerchecks",""
    "``POST``","postfix","headerchecks","set",""
    "``POST``","postfix","headerchecks","set_headercheck","$uuid"
    "``POST``","postfix","headerchecks","toggle_headercheck","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Headerchecks.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Headerchecks.xml>`__"

.. csv-table:: Resources (RecipientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","recipient","add_recipient",""
    "``POST``","postfix","recipient","del_recipient","$uuid"
    "``GET``","postfix","recipient","get",""
    "``GET``","postfix","recipient","get_recipient","$uuid=null"
    "``*``","postfix","recipient","search_recipient",""
    "``POST``","postfix","recipient","set",""
    "``POST``","postfix","recipient","set_recipient","$uuid"
    "``POST``","postfix","recipient","toggle_recipient","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Recipient.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Recipient.xml>`__"

.. csv-table:: Resources (RecipientbccController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","recipientbcc","add_recipientbcc",""
    "``POST``","postfix","recipientbcc","del_recipientbcc","$uuid"
    "``GET``","postfix","recipientbcc","get",""
    "``GET``","postfix","recipientbcc","get_recipientbcc","$uuid=null"
    "``*``","postfix","recipientbcc","search_recipientbcc",""
    "``POST``","postfix","recipientbcc","set",""
    "``POST``","postfix","recipientbcc","set_recipientbcc","$uuid"
    "``POST``","postfix","recipientbcc","toggle_recipientbcc","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Recipientbcc.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Recipientbcc.xml>`__"

.. csv-table:: Resources (SenderController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","sender","add_sender",""
    "``POST``","postfix","sender","del_sender","$uuid"
    "``GET``","postfix","sender","get",""
    "``GET``","postfix","sender","get_sender","$uuid=null"
    "``*``","postfix","sender","search_sender",""
    "``POST``","postfix","sender","set",""
    "``POST``","postfix","sender","set_sender","$uuid"
    "``POST``","postfix","sender","toggle_sender","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Sender.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Sender.xml>`__"

.. csv-table:: Resources (SenderbccController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","senderbcc","add_senderbcc",""
    "``POST``","postfix","senderbcc","del_senderbcc","$uuid"
    "``GET``","postfix","senderbcc","get",""
    "``GET``","postfix","senderbcc","get_senderbcc","$uuid=null"
    "``*``","postfix","senderbcc","search_senderbcc",""
    "``POST``","postfix","senderbcc","set",""
    "``POST``","postfix","senderbcc","set_senderbcc","$uuid"
    "``POST``","postfix","senderbcc","toggle_senderbcc","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Senderbcc.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Senderbcc.xml>`__"

.. csv-table:: Resources (SendercanonicalController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","sendercanonical","add_sendercanonical",""
    "``POST``","postfix","sendercanonical","del_sendercanonical","$uuid"
    "``GET``","postfix","sendercanonical","get",""
    "``GET``","postfix","sendercanonical","get_sendercanonical","$uuid=null"
    "``*``","postfix","sendercanonical","search_sendercanonical",""
    "``POST``","postfix","sendercanonical","set",""
    "``POST``","postfix","sendercanonical","set_sendercanonical","$uuid"
    "``POST``","postfix","sendercanonical","toggle_sendercanonical","$uuid"

    "``<<uses>>``", "", "", "", "*model* `Sendercanonical.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/Sendercanonical.xml>`__"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","postfix","service","checkrspamd",""
    "``POST``","postfix","service","reconfigure",""
    "``POST``","postfix","service","reconfigure",""
    "``POST``","postfix","service","restart",""
    "``POST``","postfix","service","start",""
    "``GET``","postfix","service","status",""
    "``POST``","postfix","service","stop",""

    "``<<uses>>``", "", "", "", "*model* `General.xml <https://github.com/opnsense/plugins/blob/master/mail/postfix/src/opnsense/mvc/app/models/OPNsense/Postfix/General.xml>`__"

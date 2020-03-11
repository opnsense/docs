Postfix
~~~~~~~

.. csv-table:: Resources (AddressController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","address","addAddress",""
    "``POST``","postfix","address","delAddress","$uuid"
    "``GET``","postfix","address","getAddress","$uuid=null"
    "``*``","postfix","address","searchAddress",""
    "``POST``","postfix","address","setAddress","$uuid"
    "``POST``","postfix","address","toggleAddress","$uuid"

.. csv-table:: Resources (DomainController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","domain","addDomain",""
    "``POST``","postfix","domain","delDomain","$uuid"
    "``GET``","postfix","domain","getDomain","$uuid=null"
    "``*``","postfix","domain","searchDomain",""
    "``POST``","postfix","domain","setDomain","$uuid"
    "``POST``","postfix","domain","toggleDomain","$uuid"

.. csv-table:: Resources (RecipientController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","recipient","addRecipient",""
    "``POST``","postfix","recipient","delRecipient","$uuid"
    "``GET``","postfix","recipient","getRecipient","$uuid=null"
    "``*``","postfix","recipient","searchRecipient",""
    "``POST``","postfix","recipient","setRecipient","$uuid"
    "``POST``","postfix","recipient","toggleRecipient","$uuid"

.. csv-table:: Resources (RecipientbccController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","recipientbcc","addRecipientbcc",""
    "``POST``","postfix","recipientbcc","delRecipientbcc","$uuid"
    "``GET``","postfix","recipientbcc","getRecipientbcc","$uuid=null"
    "``*``","postfix","recipientbcc","searchRecipientbcc",""
    "``POST``","postfix","recipientbcc","setRecipientbcc","$uuid"
    "``POST``","postfix","recipientbcc","toggleRecipientbcc","$uuid"

.. csv-table:: Resources (SenderController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","sender","addSender",""
    "``POST``","postfix","sender","delSender","$uuid"
    "``GET``","postfix","sender","getSender","$uuid=null"
    "``*``","postfix","sender","searchSender",""
    "``POST``","postfix","sender","setSender","$uuid"
    "``POST``","postfix","sender","toggleSender","$uuid"

.. csv-table:: Resources (SenderbccController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","senderbcc","addSenderbcc",""
    "``POST``","postfix","senderbcc","delSenderbcc","$uuid"
    "``GET``","postfix","senderbcc","getSenderbcc","$uuid=null"
    "``*``","postfix","senderbcc","searchSenderbcc",""
    "``POST``","postfix","senderbcc","setSenderbcc","$uuid"
    "``POST``","postfix","senderbcc","toggleSenderbcc","$uuid"

.. csv-table:: Resources (SendercanonicalController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``POST``","postfix","sendercanonical","addSendercanonical",""
    "``POST``","postfix","sendercanonical","delSendercanonical","$uuid"
    "``GET``","postfix","sendercanonical","getSendercanonical","$uuid=null"
    "``*``","postfix","sendercanonical","searchSendercanonical",""
    "``POST``","postfix","sendercanonical","setSendercanonical","$uuid"
    "``POST``","postfix","sendercanonical","toggleSendercanonical","$uuid"

.. csv-table:: Service (ServiceController.php)
   :header: "Method", "Module", "Controller", "Command", "Parameters"
   :widths: 4, 15, 15, 30, 40

    "``GET``","postfix","service","checkrspamd",""
    "``POST``","postfix","service","reconfigure",""

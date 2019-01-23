==================
Using certificates
==================

In OPNsense, certificates are used for encrypting traffic. To make using them easier, OPNsense allows creating
certificates from the front-end. In addition to that, it also allows creating certificates for other purposes,
avoiding the need to use the ``openssl`` command line tool. Certificates in OPNsense can be managed from
**System->Trust->Certificates**.

The following types of certificate can be generated in OPNsense:

* Client
* Server
* Combined Client/Server
* Certificate Authority

In addition to this, OPNsense can generate a Certificate Signing Request (CSR). This can be used if you want to create a
certficate signed by an external CA.
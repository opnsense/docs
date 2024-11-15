==================================================
Setup Self-Signed Certificate Chains
==================================================

.. contents::
   :local:
   :depth: 2

This how-to describes the process of creating **self-signed certificate chains**
with OPNsense as PKI (Public Key Infrastructure).

The following section starts with a small overview of PKI, digital certificates, and trust.


Introduction to Public Key Infrastructure (PKI)
==================================================

A **Public Key Infrastructure (PKI)** is a framework used to manage digital keys and certificates. PKI supports **asymmetric encryption**, where two related keys – a public key and a private key – are used together to secure communications and authenticate users.

OPNsense provides its own PKI in :menuselection:`System --> Trust`.


Components of PKI
-----------------

- **Certificate Authority (CA)**: The trusted entity that issues and verifies digital certificates.
- **Registration Authority (RA)**: Assists the CA by verifying entities before certificates are issued.
- **Digital Certificates**: Bind public keys to individuals or entities, confirming identity.
- **Certificate Revocation List (CRL)**: A list of certificates that have been revoked, used to manage trust.

When creating and using your own PKI, the above components depend on compliance. When you are a home user or manage a small company network, these can all be fulfilled by a single person or a small team. In large infrastructures, PKI management needs careful considerations.


How PKI Works
-------------

1. The CA issues a digital certificate containing the entity's public key.
2. A sender uses the public key to encrypt information sent to the certificate holder.
3. The certificate holder uses their private key to decrypt the information.
4. Digital signatures can also be created with the private key and verified by others using the public key.

Together, PKI enables secure data exchange, authentication, and digital identity verification.


Public and Private Keys
-----------------------

In PKI, each entity has a unique pair of cryptographic keys:

- **Public Key**: The public key is shared openly. It is used to encrypt data that can only be decrypted by the matching private key. It is also used to verify digital signatures created by the private key. Public keys are included in digital certificates to enable secure exchanges.

- **Private Key**: The private key is kept secret by the owner. It decrypts data that was encrypted with the matching public key and creates digital signatures that can be verified by the public key. Protecting the private key is essential.


Understanding Trust
---------------------------------------

Trust in certificates refers to the confidence that the certificate’s issuer has verified identity and authenticity.
This is less of a technical term, but trust between either real people or organizations who issue and verify certificates.
The actual action of trust is when you install a CA certificate in your operating systems trust store. If the CA certificate has been pre-installed by
a third party organization, you trust that organization by keeping it in your trust store.

**Trust in CA-Issued Certificates**

When using a CA-issued certificate, trust is based on identity verification, as the CA verifies the identity of certificate requesters; compliance, as CAs follow industry standards and are regularly audited; and widespread recognition, since CA root certificates are pre-trusted in most systems.

**Trust in Self-Signed Certificates**

For self-signed certificates, trust relies on the issuer’s security practices and if you want to trust their self-signed CA.
Users must accept or install the certificate in their operating system trust store.
Compromise of a self-signed certificate has higher risks, as there is likely no automatic revocation process.
Using them for publicly accessible services introduces constraints due to lack of third-party validation and automatic trust.


Certificate Chains
--------------------------------------------

Certificate chains enable verification of multiple levels of certificates, rather than relying on the validation of a single, isolated certificate.

Should you consider using self-signed certificate chains when free and widely recognized certificates are readily available?

- Self-signed certificates can be just as secure as publicly trusted certificates.
- They establish a chain of trust, where each party is well-known and directly controlled.
- You have full control of the PKI and the validity of each certificate. No external party can invalidate the certificates.

For a functional certificate chain, you will need at least a root CA and a leaf certificate (end-entity certificate). An intermediate CA is not required but adds a layer of security: if compromised, only the intermediate CA is affected, protecting the root CA key.

.. Attention::

    To enhance security:

    - Store the root CA private key offline, such as on a USB or secure drive, kept in a safe location inaccessible to potential malware or unauthorized access.
    - Keep multiple copies of the private key in different locations.
    - The intermediate CA, generally with a shorter lifecycle, may be stored on a firewall host.


Creating a Certificate Chain
====================================

We will create a certificate chain using the following components:

- **Root CA**: Self-signed → Signs intermediate certificates
- **Intermediate CA**: Signed by the Root CA → Signs leaf certificates
- **Leaf Certificate**: Signed by the Intermediate CA → Server or user certificate

**Important**: Ensure all data is backed up before proceeding.

Here is an overview of the available GUI options:

.. tabs::

    .. tab:: Authorities

       :menuselection:`System --> Trust --> Authorities`

       ===================================== =======================================================================================================================
       **Options**                           **Description**
       ===================================== =======================================================================================================================
       **Method**                            The operation to perform, such as creating a new CA, importing an existing one, or generating a Certificate Signing Request (CSR).
       **Description**                       A brief identifier or label for the CA to distinguish it from others.
       **Key**                               Configuration settings related to the cryptographic key associated with the CA.
       **Key Type**                          The algorithm and size of the key pair (e.g., RSA 2048-bit, ECDSA).
       **Digest Algorithm**                  The hash function used in the digital signature process (e.g., SHA-256).
       **Issuer**                            The entity that signs the CA certificate; for a root CA, this is self-signed.
       **Lifetime (days)**                   The validity period of the CA certificate, specified in days.
       **General**                           General information fields for the CA's Distinguished Name (DN).
       **Country Code**                      The two-letter ISO code representing the country (e.g., 'DE' for Germany).
       **State or Province**                 The full name of the state or province.
       **City**                              The locality or city name.
       **Organization**                      The legal name of the organization.
       **Organizational Unit**               A subdivision or department within the organization.
       **Email Address**                     Contact email for the CA administrator.
       **Common Name**                       The primary identifier for the CA, often its fully qualified domain name (FQDN).
       **OCSP URI**                          The URL where the Online Certificate Status Protocol responder can be reached for certificate status checking.
       **Output (PEM format)**               The resulting certificate and key data in PEM format.
       **Certificate Data**                  The CA's public certificate in PEM format.
       **Private Key Data**                  The CA's private key in PEM format; handle with strict security measures.
       **Serial for Next Certificate**       The starting serial number for certificates issued by this CA; it increments with each issued certificate.
       ===================================== =======================================================================================================================

       .. Note:: This is where root or intermediate certificate authorities are created or imported.


    .. tab:: Certificates

       :menuselection:`System --> Trust --> Certificates`

       ===================================== =======================================================================================================================
       **Options**                           **Description**
       ===================================== =======================================================================================================================
       **Method**                            The action to perform, such as creating, importing, or signing a CSR for a leaf certificate.
       **Description**                       A label or identifier for the certificate to distinguish it from others.
       **Key**                               Settings related to the cryptographic key for the certificate.
       **Type**                              The purpose of the certificate (e.g., server authentication, client authentication).
       **Private Key Location**              Specifies where the private key is stored or generated.
       **Key Type**                          The algorithm and size of the key pair (e.g., RSA 2048-bit, ECDSA).
       **Digest Algorithm**                  The hash function used in the digital signature process (e.g., SHA-256).
       **Issuer**                            The CA that signs and issues the certificate.
       **Lifetime (days)**                   The validity period of the certificate, specified in days.
       **General**                           General information fields for the certificate's Distinguished Name (DN).
       **Country Code**                      The two-letter ISO code representing the country.
       **State or Province**                 The full name of the state or province.
       **City**                              The locality or city name.
       **Organization**                      The legal name of the organization.
       **Organizational Unit**               A subdivision or department within the organization.
       **Email Address**                     Contact email for the certificate subject.
       **Common Name**                       The primary identifier for the certificate, often the FQDN of the server or the name of the individual.
       **OCSP URI**                          The URL where the OCSP responder can be reached for certificate status checking.
       **Alternative Names**                 Additional identifiers for the certificate subject.
       **DNS Domain Names**                  Alternative domain names covered by the certificate.
       **IP Addresses**                      IP addresses associated with the certificate subject.
       **URIs**                              Uniform Resource Identifiers associated with the certificate subject.
       **Email Addresses**                   Additional email addresses associated with the certificate subject.
       **Output (PEM format)**               The resulting certificate and key data in PEM format.
       **Certificate Data**                  The leaf certificate's public certificate in PEM format.
       **Private Key Data**                  The leaf certificate's private key in PEM format; handle with strict security measures.
       **Certificate Signing Request**       A CSR containing the public key and Distinguished Name to be signed by a CA.
       ===================================== =======================================================================================================================

       .. Note:: This is where leaf certificates signed by intermediate or root certificate authorities are created or imported.


    .. tab:: Revocation

       :menuselection:`System --> Trust --> Revocation`

       ===================================== =======================================================================================================================
       **Options**                           **Description**
       ===================================== =======================================================================================================================
       **Method**                            The operation to perform, such as creating a new CRL or importing an existing one.
       **CA Reference**                      The CA associated with this CRL.
       **Description**                       A brief description or identifier for this CRL.
       **CRL Data**                          Contains the actual CRL in PEM format, listing revoked certificates and their statuses.
       **Serial**                            The unique serial number identifying the certificate to be revoked.
       **Lifetime (days)**                   Specifies how long the CRL is valid before it needs to be regenerated.
       **Revocations per type**              Specifies reasons for revocation as categories (e.g., Unspecified, Key Compromise, CA Compromise).
       **Unspecified**                       Indicates a certificate was revoked without a specified reason.
       **Key Compromise**                    Indicates the private key associated with the certificate was compromised.
       **CA Compromise**                     Indicates that the issuing CA's private key was compromised.
       **Affiliation Changed**               Indicates that the certificate subject's affiliation with the organization has changed.
       **Superseded**                        Indicates that the certificate was replaced by another.
       **Cessation of Operation**            Indicates that the entity associated with the certificate no longer operates.
       **Certificate Hold**                  Temporarily revokes a certificate, which may be reinstated later.
       ===================================== =======================================================================================================================

       .. Note:: This is where certificate revocation lists for certificates signed by intermediate or root certificate authorities are created or imported.


    .. tab:: Settings

       :menuselection:`System --> Trust --> Settings`

       ===================================== =======================================================================================================================
       Options                               Description
       ===================================== =======================================================================================================================
       **Store intermediate**                Allow local defined intermediate certificate authorities to be used in the local trust store.
                                             We advise to only store root certificates to prevent cross signed ones causing breakage
                                             when included but expired later in the chain.
       **Store CRL's**                       Store all configured CRL's in the default trust store.
       **Auto fetch CRL's**                  Schedule an hourly job to download CRLs using the defined Distributionpoints in the CAs deployed in our trust store.
       **Enable legacy**                     Enable Legacy Providers.
       **Enable**                            Enable custom constraints.
       **CipherString**                      Sets the ciphersuite list for TLSv1.2 and below.
       **Ciphersuites**                      Sets the available ciphersuites for TLSv1.3.
       **SignatureAlgorithms**               Sets the available SignatureAlgorithms.
       **DHGroups / Curves**                 Limit the default set of built-in curves to be used when using the standard openssl configuration.
       **MinProtocol**                       Sets the minimum supported SSL or TLS version.
       **MinProtocol (DTLS)**                Sets the minimum supported DTLS version. When configuring MinProtocol and leaving this empty,
                                             DTLS will be disabled.
       ===================================== =======================================================================================================================


Step 1: Creating the Root CA
-----------------------------------------

Go to :menuselection:`System --> Trust --> Authorities`

Press **+** to create a new authority, it will become your root certificate authority.

===================================== =======================================================================================================================
**Options**                           **Description**
===================================== =======================================================================================================================
**Method**                            ``Create an internal Certificate Authority``
**Description**                       ``Root CA`` (or a custom description)
**Key**
**Key Type**                          ``RSA-2048`` (or higher)
**Digest Algorithm**                  ``SHA256`` (or higher)
**Issuer**                            ``self-signed`` (root CA is always self-signed)
**Lifetime (days)**                   ``3650`` (after this expires the root CA, all its issued intermediate CA their issued leaf certificates must be recreated)
**General**
**Country Code**                      ``Netherlands`` (your country)
**State or Province**                 ``Zuid-Holland`` (your state or empty)
**City**                              ``Middelharnis`` (your city or empty)
**Organization**                      ``Deciso B.V.`` (your organization name or empty)
**Organizational Unit**               ``IT`` (your organizational unit or leave empty)
**Email Address**                     ``info@example.com`` (your email address, it is best practice to use a real existing one)
**Common Name**                       ``root-ca`` (or a custom name)
**OCSP URI**                          `leave empty`
===================================== =======================================================================================================================

Press **Save** and the root CA has been created. The private and public key are saved on the OPNsense.


Step 2: Issuing the Intermediate CA
-----------------------------------------

Go to :menuselection:`System --> Trust --> Authorities`

Press **+** to create a new authority, it will become your intermediate certificate authority.

===================================== =======================================================================================================================
**Options**                           **Description**
===================================== =======================================================================================================================
**Method**                            ``Create an internal Certificate Authority``
**Description**                       ``Intermediate CA`` (or a custom description)
**Key**
**Key Type**                          ``RSA-2048`` (or higher)
**Digest Algorithm**                  ``SHA256`` (or higher)
**Issuer**                            ``Root CA`` (The intermediate CA is always signed by the Root CA)
**Lifetime (days)**                   ``1095`` (after this expires the intermediate CA and all its issued leaf certificates must be recreated)
**General**
**Country Code**                      ``Netherlands`` (your country)
**State or Province**                 ``Zuid-Holland`` (your state or empty)
**City**                              ``Middelharnis`` (your city or empty)
**Organization**                      ``Deciso B.V.`` (your organization name or empty)
**Organizational Unit**               ``IT`` (your organizational unit or leave empty)
**Email Address**                     ``info@example.com`` (your email address, it is best practice to use a real existing one)
**Common Name**                       ``intermediate-ca`` (or a custom name)
**OCSP URI**                          `leave empty`
===================================== =======================================================================================================================

Press **Save** and the intermediate CA has been created. The private and public key are saved on the OPNsense.


Step 3: Issuing a Leaf Certificate
-----------------------------------------

Go to :menuselection:`System --> Trust --> Certificates`

Press **+** to create a new authority, it will become your leaf certificate (end-entity certificate).
It can be used on a server, user, or both; depending on the type.

===================================== =======================================================================================================================
**Options**                           **Description**
===================================== =======================================================================================================================
**Method**                            ``Create an internal Certificate``
**Description**                       ``leaf-certificate.example.com`` (or a custom description, like user or server name)
**Key**
**Type**                              ``Server Certificate`` (or client certificate for a user)
**Private Key Location**              ``Save on this firewall``
**Key Type**                          ``RSA-2048`` (or higher)
**Digest Algorithm**                  ``SHA256`` (or higher)
**Issuer**                            ``Intermediate CA``
**Lifetime (days)**                   ``365`` (after this expires the leaf certificate must be recreated)
**General**
**Country Code**                      ``Netherlands`` (your country)
**State or Province**                 ``Zuid-Holland`` (your state or empty)
**City**                              ``Middelharnis`` (your city or empty)
**Organization**                      ``Deciso B.V.`` (your organization name or empty)
**Organizational Unit**               ``IT`` (your organizational unit or leave empty)
**Email Address**                     ``info@example.com`` (your email address, it is best practice to use a real existing one)
**Common Name**                       ``leaf-certificate.example.com`` (or a custom name)
**OCSP URI**                          `leave empty`
**Alternative Names**
**DNS Domain Names**                  ``leaf-certificate.example.com`` (or a custom name)
===================================== =======================================================================================================================

Press **Save** and the leaf certificate has been created. The private and public key are saved on the OPNsense.

.. Note::

   The private key does not have to be stored. For higher security, only download it by setting the Private Key Location to the alternative option.
   This way, the private key can be installed on the required server without a copy in the OPNsense trust store.
   To issue leaf certificates, only the Intermediate CAs need their private keys stored in the trust store.

The next step will be exporting the certificate chain, and using the leaf certificate on an external webserver.


Step 4: Exporting the Certificate Chain
-----------------------------------------

Now that we have the whole certificate chain, we create a certificate bundle for a generic linux apache web server.

For that, we need two files:

- A certificate bundle populated in the correct order in PEM format:

    #. Root CA
    #. Intermediate CA
    #. Leaf Certificate

- The private key of the leaf certificate

#. Export Root CA public key:

    - Go to :menuselection:`System --> Trust --> Authorities`
    - Press the download button in the `Commands` column of the ``Root CA`` row
    - Choose `File type: Certificate` and press `Download`

#. Export Intermediate CA public key:

    - Go to :menuselection:`System --> Trust --> Authorities`
    - Press the download button in the `Commands` column of the ``Intermediate CA`` row
    - Choose `File type: Certificate` and press `Download`

#. Export Leaf Certificate public key:

    - Go to :menuselection:`System --> Trust --> Certificates`
    - Press the download button in the `Commands` column of the ``Leaf Certificate`` row
    - Choose `File type: Certificate` and press `Download`

#. Export Leaf Certificate private key:

    - Go to :menuselection:`System --> Trust --> Certificates`
    - Press the download button in the `Commands` column of the ``Leaf Certificate`` row
    - Choose `File type: Private Key` and press `Download`

Open a text editor and create a file with all 3 public keys:

``certificate-bundle.pem``

.. code-block::

    -----BEGIN CERTIFICATE-----
    Root CA public key data
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    Intermediate CA public key data
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    Leaf Certificate public key data
    -----END CERTIFICATE-----

The key of the certificate bundle is only the leaf certificate's private key. Private keys of root and intermediate CAs are **not** required.

``certificate-bundle.key``

.. code-block::

    -----BEGIN PRIVATE KEY-----
    Leaf Certificate private key data
    -----END PRIVATE KEY-----

Implement these into your webserver, and the website will be secured with this certificate bundle.
For automatic trust, you must install the intermediate and/or root CA certificate public keys into any client that connects to the webserver.
Since the webserver offers a full certificate chain to the connecting client, manual trust can be established if a user decides to install the public key themselves.

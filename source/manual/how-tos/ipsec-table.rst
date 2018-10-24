VPN compatibility table
~~~~~~~~~~~~~~~~~~~~~~~

Here you can find a compatibility table for all general operating systems. 
For Linux testing was done with Ubuntu 18.4 Desktop and XdebX installed. 
As Andoid doe not support IKEv2 yet we added notes for combinations with strongswan
app installed to have a broader compatibility for all systems.

.. csv-table:: VPN combinations
   :header: "VPN Method", "Win7", "Win10", "Linux", "Mac OS X", "IOS", "Android"
   :widths: 40, 10, 10, 10, 10, 10, 30

   "IKEv1 Hybrid RSA + XAuth","N","N","Yes","Yes","Yes","Yes"
   "IKEv1 Mutual RSA + XAuth","N","N","Yes","Yes","Yes","Yes"
   "IKEv1 Hybrid PSK + XAuth","N","N","tbd","tbd","tbd","tbd"
   "IKEv2 EAP-TLS","tbd","tbd","tbd","tbd","tbd","tbd"
   "IKEv2 RSA local + EAP remote","tbd","tbd","tbd","tbd","tbd","tbd"
   "IKEv2 EAP-MSCHAPv2","Y","Y","Y","Y","Y","Y, with Strongswan"
   "IKEv2 Mutual RSA + EAP-MSCHAPv2","tbd","tbd","tbd","tbd","tbd","tbd"
   "IKEv2 EAP-RADIUS","Y","Y","Y","Y","Y","Y, with Strongswan"
   "IKEv1 Mutual RSA","N","N","N","N","N","N"
   "IKEv1 Mutual PSK","N","N","N","N","N","N"


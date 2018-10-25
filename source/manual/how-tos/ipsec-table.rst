VPN compatibility table
~~~~~~~~~~~~~~~~~~~~~~~

Here you can find a compatibility table for all general operating systems. 
For Linux testing was done with Ubuntu 18.4 Desktop and XdebX installed. 
As Andoid doe not support IKEv2 yet we added notes for combinations with strongswan
app installed to have a broader compatibility for all systems.

.. csv-table:: VPN combinations
   :header: "VPN Method", "Win7", "Win10", "Linux", "Mac OS X", "IOS", "Android", "OPNsense config"
   :widths: 40, 10, 10, 10, 10, 10, 20, 20

   "IKEv1 Hybrid RSA + XAuth","N","N","Yes","Yes","Yes","Yes","Link"
   "IKEv1 Mutual RSA + XAuth","N","N","Yes","Yes","Yes","Yes","Link"
   "IKEv1 Hybrid PSK + XAuth","N","N","tbd","tbd","tbd","tbd","Link"
   "IKEv2 EAP-TLS","tbd","tbd","tbd","tbd","tbd","tbd","Link"
   "IKEv2 RSA local + EAP remote","tbd","tbd","tbd","tbd","tbd","tbd","Link"
   "IKEv2 EAP-MSCHAPv2","Y","Y","Y","Y","Y","Y, w/ Strongswan","Link"
   "IKEv2 Mutual RSA + EAP-MSCHAPv2","tbd","tbd","tbd","tbd","tbd","tbd","Link"
   "IKEv2 EAP-RADIUS","Y","Y","Y","Y","Y","Y, w/ Strongswan","Link"
   "IKEv1 Mutual RSA","N","N","N","N","N","N","Link"
   "IKEv1 Mutual PSK","N","N","N","N","N","N","Link"


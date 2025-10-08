*************************
**IPinfo GeoIP's Setup**
*************************

When using IPinfo as your GeoIP provider, you can use this howto to set up your data feeds.

###################
Create An Account
###################


Goto https://ipinfo.io/signup and create your account.

######################
Collect the link
######################

Once you have created an account you'll need to find your license key.
The easiest process is to login to IPinfo and go to https://ipinfo.io/dashboard/downloads

On the right side of the screen you will notice a big download button, choose the prop format in the tabs above (we need **csv**)
and use the copy link button next to the download one.

On your clipboard there's a link which looks like:

    https://ipinfo.io/data/ipinfo_lite.csv.gz?token=XXXXXXXX



##########
OPNsense
##########

In OPNsense, goto Firewall:Aliases and select the GeoIP settings tab. Enter the URL you have collected into the URL box and click Apply.

Once you have set up the IPalias credentials if you have not created a GeoIP alias you will need to do so.
Instructions on how to create the alias(es) can be found in the Firewall->Aliases section of our documentation.

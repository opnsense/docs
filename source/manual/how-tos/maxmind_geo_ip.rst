*************************
**MaxMind GeoIP's Setup**
*************************

With the changes MaxMind have implemented it is now a requirement that anyone using their lists must have an account and by having that account will have accepted their data protection requirements. It's fairly simple to set-up so let's get started.

###################
Create An Account
###################

Goto https://www.maxmind.com/en/geolite2/signup and create your account. Note that the email address you provide will be used to send you the link you will need to enter in OPNsense, so make sure its a real account.

######################
Generate License Key
######################

Once you have created an account you'll need to create a license key. Click in the "My License Key" link and generate a key. When asked if you use "geoipupdate",  choose "no". Save the key ID somewhere safe!!!

You do not need to download the config at this point.

#############
Create Link
#############

Now, we need to create the link we'll need in OPNsense; all you need to do now is replace the 'AccountID' and 'LicenseKey' parts of the link below with your account ID and license key, respectively.

https://AccountID:LicenseKey@download.maxmind.com/geoip/databases/GeoLite2-Country-CSV/download?suffix=zip

You can check that you have done it correctly by just pasting the link into a browser, it should download the zip file.


##########
OPNsense
##########

In OPNsense, goto Firewall:Aliases and select the GeoIP settings tab. Enter the URL you have created into the URL box and click Apply.

Once you have set up the Maxmind credentials if you have not created a GeoIP alias you will need to do so. Instructions on how to create the alias(es) can be found in the Firewall->Aliases section of this wiki.

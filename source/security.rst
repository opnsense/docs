====================================
Security
====================================

.. contents:: Index


------------------------------------------------------------
Intro
------------------------------------------------------------

As your trusted opensource security product, we do care a lot about security and with our regular release schedule we
try to stay ahead of possible incidents. Even though we are cautious and stay informed, sometimes issues
do ocure, in which case it's good to know what to do.


------------------------------------------------------------
Staying ahead
------------------------------------------------------------

Even though we always encourage people to update regularly, sometimes it's not possible to do so for various reasons.

Luckily OPNsense comes with an integrated security check for know vulnerabilities, which can be found in our firmware
module. In which case you do have the opportunity to validate for yourself what the risk is to keep using the
current version for a bit longer.

You can reach it via :menuselection:`System -> Firmware` in the status pane, the button "Run an Audit"
will bring you right into the security report.

If all goes well, a report like the one below will be shown:

.. code-block::

    ***GOT REQUEST TO AUDIT SECURITY***
    Currently running OPNsense 22.1.8_1 (amd64/OpenSSL) at Tue May 31 09:01:04 CEST 2022
    vulnxml file up-to-date
    0 problem(s) in 0 installed package(s) found.
    ***DONE***


.. Note::

    We do not offer community support on assessing if incidents on older versions do warrant an immediate upgrade on your
    end as this often depends on features used and settings configured. Our advise always will be to upgrade into the
    latest community or business version.


.. Warning::

    Please don't report issues to us reported by the security health check, they are already known and highly likely
    a fix is pending for the next release.


------------------------------------------------------------
Upstream vulnerabilities
------------------------------------------------------------

Since OPNsense is a collection of opensource software, when finding an issue, it is always a good idea to
inspect where is should be fixed first. In case you don't know or aren't sure, you can still ask on our end, just
know that we don't have the manpower to act as an intermediate between various projects.


------------------------------------------------------------
Reporting an incident
------------------------------------------------------------

Security incidents on our product can be reported to our security team available at **security** @ **opnsense.org**.

All reports should contain at least the following information:

* A clear description of the vulnerability at hand
* Which version(s) of our product seem to be affected
* Any known workaround
* When possible, some example code

Our GPG information for delivering encrypted emails is as follows:

* GPG Key ID: D3C7FBDB
* GPG Fingerprint: 97D5 0C7F EC38 22D0 85AE  51B1 C271 8D7A D3C7 FBDB

------------------------------------------------------------
Information handling policies
------------------------------------------------------------

As a general policy we do favor full disclosure of vulnerability information after a reasonable amount of time to permit
safe analysis and correction as well as appropriate testing for the correction at hand.

In order to coordinate with other affected parties, we might share parts of the information provided to us to them as well
or ask the reporter to do so.

When the submitter is interested in a coordinated disclosure process, this should be indicated in any submission to avoid
discussions later on.

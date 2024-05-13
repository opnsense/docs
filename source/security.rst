====================================
Security
====================================

.. contents:: Index


------------------------------------------------------------
Intro
------------------------------------------------------------

As your trusted opensource security product, we do care a lot about security and with our regular release schedule we
try to stay ahead of possible incidents. Even though we are cautious and stay informed, sometimes issues
do occur, in which case it's good to know what to do.


------------------------------------------------------------
Staying ahead
------------------------------------------------------------

Even though we always encourage people to update regularly, sometimes it's not possible to do so for various reasons.

Luckily OPNsense comes with an integrated security check for known vulnerabilities, which can be found in our firmware
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


------------------------------------------------------------
Information handling policies
------------------------------------------------------------

As a general policy we do favor full disclosure of vulnerability information after a reasonable amount of time to permit
safe analysis and correction as well as appropriate testing for the correction at hand.

In order to coordinate with other affected parties, we might share parts of the information provided to us to them as well
or ask the reporter to do so.

When the submitter is interested in a coordinated disclosure process, this should be indicated in any submission to avoid
discussions later on.


------------------------------------------------------------
Third party security verification
------------------------------------------------------------

Intro
............................................................

Within the OPNsense team and community we spend a lot of time safeguarding our software and keeping up with the latest threats,
like checking used software against CVE's on every release, implementing best practices in our development methods and
offering clear and transparent release engineering.

To even improve this further, we decided to bring a third party on board and mold a process around our security verification
by trained security professionals.


Business Edition
............................................................

As our business edition is aimed at professional users, it does make sense to offer additional safeguards, like even more extensive testing on
this product. Looking at the lifecycle of our software, this is also the most mature stage of what we do have to offer:

* Development version

  -  Available at every release, offers a glimpse of what to expect in the near future

* Community version

  - When changes survive the development version, these are included in the community version, these are internally tested and
    feedback has been offered by community members.

* Business Edition

  - Functional changes are being included in a more conservative manner, more feedback has been collected from development
    and community, leading to a mission critical version of your well known OPNsense firewall.

As security testing is quite time-consuming, we aim to offer a full qualification cycle at every major release.


Framework / Type of testing (LINCE)
............................................................

In our quest for a framework to use, we found the LINCE methodology.

LINCE is a lightweight methodology for evaluating and certifying ICT products, created by Spain's National Cryptologic Center (`CCN <https://www.ccn.cni.es/index.php/en/menu-ccn-en>`__),
based on Common Criteria principles and oriented to vulnerability analysis and penetration tests.

LINCE strengths over other methodologies mainly consist of reduced effort and duration.
However, the way in which it is applied also makes it possible to pay more attention to the critical points of each product,
giving more weight to concrete and practical tests that combat real threats than to dense documentation or exhaustive functionality tests.

As most frameworks are not intended to be repeated very regularly, together with `jtsec <https://www.jtsec.es/>`__ we came up with an approach which
makes it possible to pass the test twice a year, which is needed to align with our Business Edition releases.

During every cycle, there's always a chance that (small) issues appear which should be fixed, in close accordance with jtsec, the OPNSense
team prepares fixes for the findings and makes sure that these are included in a future (minor) release.


Steps in the process
............................................................
To better understand where a version of OPNsense is at in terms of verification, we distinct the following stages in the process, which
we will also note on the version at hand.

1.  In test - Software delivered to jtsec, in process (interaction between OPNsense and jtsec).
2.  Tested - Software verified / tested, documentation not yet published.
3.  LINCE Compliant - Test complete including summarised report (by jtsec)
4.  Certification pending - Offered for formal certification. (as of 2023)
5.  LINCE Certified - Certified by CCN (as of 2023)

The certification steps are planned to be executed once a year starting in 2023, this process is quite time consuming, but
adds another independent party to the mix.

Timeline
............................................................
The first fully certified product has been a community version (21.7.1), which offered us insights into the process and
helped us improve the process which we would like to use for the business edition. We started this cycle with version 22.4
including full testing by jtsec and made plans for the future.

Results
............................................................

Below you will find the versions that have been tested or are currently in test.

+----------+-----------------------+------------------------------------------------------------------------------------------------------+
| Version  | status                | Download                                                                                             |
+==========+=======================+======================================================================================================+
| BE 23.10 | Certification pending | report available after CCN approval                                                                  |
+----------+-----------------------+------------------------------------------------------------------------------------------------------+
| BE 23.04 | LINCE Compliant       | :download:`BR23.04-STIC_OPNSENSE_CQ-ETR-v3.1.pdf <pdf/BE23.04-STIC_OPNSENSE_CQ-ETR-v3.1.pdf>`        |
|          |                       | 9cce20526a25de2f03b29dcb80df8277eac4eb02066e504396c07e0caffd104e                                     |
+----------+-----------------------+------------------------------------------------------------------------------------------------------+
| BE 22.10 | LINCE Compliant       | :download:`BE22.10-STIC_OPNSENSE_CQ-ETR-v2.0.pdf <pdf/BE22.10-STIC_OPNSENSE_CQ-ETR-v2.0.pdf>`        |
|          |                       | 6fae801d18c3c8574ab8cca9a6f03f8b898dbe8a22136ee8fc8aa01173539fb4                                     |
+----------+-----------------------+------------------------------------------------------------------------------------------------------+
| BE 22.04 | LINCE Compliant       | :download:`BE22.04-STIC_OPNSENSE_CQ-ETR-v1.0.pdf <pdf/BE22.04-STIC_OPNSENSE_CQ-ETR-v1.0.pdf>`        |
|          |                       | 5b303285f3b9f9cd6290a623d7c509e48c59da4c678884a1513e84ee7d06d5d1                                     |
+----------+-----------------------+------------------------------------------------------------------------------------------------------+


External references
............................................................

* https://www.jtsec.es/product-security-testing

  -  `Standard definitions <https://www.jtsec.es/files/CCN-LINCE-001_v0.1_final_EN.pdf>`__
  -  `Evaluation methodology <https://www.jtsec.es/files/CCN-LINCE-002_v0.1_final_EN.pdf>`__

* https://www.ccn.cni.es/index.php/en/menu-ccn-en
* https://oc.ccn.cni.es/en/certified-products/certified-products

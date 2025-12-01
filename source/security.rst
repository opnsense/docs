====================================
Security
====================================

.. contents:: Index


------------------------------------------------------------
Introduction
------------------------------------------------------------

As a trusted open-source security platform, we care a lot about security and, with our regular release schedule, we
try to stay ahead of any potential vulnerabilities. Even though we are cautious and try to stay informed, problems can and
do occur, in which case it is good to know what to do.


------------------------------------------------------------
Staying ahead
------------------------------------------------------------

Although we always encourage people to update regularly, we understand that sometimes it is not feasible to do so for
one reason or another.

Fortunately, OPNsense comes with an integrated security audit for known vulnerabilities, available in the Firmware
section. This allows you to assess for yourself what the risk is when deciding to keep running the
current version instead of updating.

You can find this tool by going to :menuselection:`System -> Firmware -> Status`. Here, by clicking the button "Run an Audit"
then "Security", it will scan the system and generate a security report like the one below if successful:

.. code-block::

    ***GOT REQUEST TO AUDIT SECURITY***
    Currently running OPNsense 22.1.8_1 (amd64/OpenSSL) at Tue May 31 09:01:04 CEST 2022
    vulnxml file up-to-date
    0 problem(s) in 0 installed package(s) found.
    ***DONE***


.. Note::

    We do not offer community support for assessing whether incidents on older versions warrant an immediate upgrade
    as this often depends on the features used and settings configured. Our advice will always be to upgrade to the
    latest community or business version.


.. Warning::

    Please do not report issues to us reported by the security audit as they are already known and likely
    to have a fix pending for the next release.


------------------------------------------------------------
Upstream vulnerabilities
------------------------------------------------------------

Since OPNsense is a collection of open-source software, when discovering an issue, it is always a good idea to
find where it should be fixed first. In case you are not sure, you can still ask on our end, just
keep in mind that we do not have the manpower needed to act as an intermediary between various projects.


------------------------------------------------------------
Reporting an incident
------------------------------------------------------------

Security vulnerabilities in OPNsense can be reported on the `GitHub repository <https://github.com/opnsense/core/security>`__.
You may also create a new issue and select "Report a security vulnerability", which will redirect you to the same page.
Alternatively, you can report security issues to our security team via **security** @ **opnsense.org**.

All reports should contain at least the following information:

* A clear description of the vulnerability at hand
* Which versions of OPNsense appear to be affected
* Any known workarounds or temporary fixes
* If possible, code snippets affected by or containing the vulnerability


------------------------------------------------------------
Information handling policy
------------------------------------------------------------

As a general policy, we favor the full disclosure of vulnerability information after a reasonable amount of time to permit
safe analysis and correction, as well as appropriate testing of the correction.

In order to coordinate with other affected parties, we may share parts of the information provided to us with them as well,
or we may ask the submitter to do so.

When the submitter is interested in a coordinated disclosure process, this should be indicated in any submission to avoid
misunderstandings later on.


------------------------------------------------------------
Third party security verification
------------------------------------------------------------

Intro
............................................................

Within the OPNsense team and community, we spend a lot of time safeguarding our software and keeping up with the latest threats,
like checking used software against CVEs on every release, implementing best practices in our development methods and
offering clear and transparent release engineering.

To improve this even further, we decided to bring a third party on board and mold a process around our security verification
by trained security professionals.


Business Edition
............................................................

As the Business Edition is built around professional use, it makes sense to offer additional safeguards like even more extensive testing on
Business Edition releases. Looking at the lifecycle of OPNsense, this is also the most mature stage of what we have to offer:

* Development version

  -  Available at every release, it offers a glimpse of what to expect in the near future.

* Community version

  - When changes have passed through the development version, they are included in the community version, where they are
    internally tested and feedback provided by community members.

* Business Edition

  - Functional changes are included in a more conservative manner, with additional feedback collected from development
    and the community, resulting in a mission-critical version of the OPNsense firewall.

As security testing is quite time-consuming, we aim to offer a full qualification cycle for every major release.


Framework / Type of testing (LINCE)
............................................................

In our quest for a framework to use, we found the LINCE methodology.

LINCE is a lightweight methodology for evaluating and certifying ICT products, created by Spain's National Cryptologic Center (`CCN <https://cpstic.ccn.cni.es/en/>`__),
based on Common Criteria principles and oriented around vulnerability analysis and penetration tests.

LINCE's strengths over other methodologies mainly lie in its reduced effort and shorter duration.
However, the way in which it is applied also makes it possible for us to pay more attention to the more critical areas of our product,
giving more weight to concrete and practical tests that address real threats than to dense documentation or exhaustive functionality tests.

As most frameworks are not intended to be repeated very regularly, together with `jtsec <https://www.jtsec.es/>`__, we came up with an approach which
makes it possible to pass the test twice a year, which is needed to align with our Business Edition releases.

During every cycle, there is always a chance that minor issues appear which should be fixed, and in close accordance with jtsec, the OPNsense
team prepares fixes for the findings and makes sure that these are included in a future (minor) release.


Steps in the process
............................................................
To better understand where a version of OPNsense is at in terms of verification, we distinguish the following stages in the process, which
we will also note on the version at hand.

1.  In testing - Software delivered to jtsec, in process (interaction between OPNsense and jtsec).
2.  Tested - Software verified / tested, documentation not yet published.
3.  LINCE Compliant - Test complete including a summarised report (by jtsec).
4.  Certification pending - Offered for formal certification.
5.  LINCE Certified - Certified by CCN.

These certification steps are executed twice a year, once for each Business Edition release. This process is relatively time consuming, but it
adds another independent layer of assurance.

Timeline
............................................................
The first fully certified product is a community version (21.7.1), which offered us insights into the process and
helped us improve the process for what we would like to use with the Business Edition. We started this cycle with version 22.4
including full testing by jtsec.

Results
............................................................

Below you will find the versions that have been tested or are currently in testing.


+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| Version  | Status                | Download                                                                                                   |
+==========+=======================+============================================================================================================+
| BE 25.10 | LINCE Compliant       | :download:`BE25.10-OPNSENSE_IAD-2510_v1.0.pdf <pdf/BE25.10-OPNSENSE_IAD-2510_v1.0.pdf>`                    |
|          |                       | 1a927d96fc7a4fb44323c79cacc8cda75cfe5824a61c3a9a2064b02acf4b0023                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| BE 25.04 | LINCE Certified       | :download:`BE25.4-STIC_OPNSENSE_IAD-2504-ETR-v1.0.pdf <pdf/BE25.4-STIC_OPNSENSE_IAD-2504-ETR-v1.0.pdf>`    |
|          |                       | 591a63be0f6f4e8d15c1b6fe2ea48af3e5dd1234f7b9013ffec6cd7b89d3d95f                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| BE 24.10 | LINCE Certified       | :download:`BE24.10-STIC_OPNSENSE_HIGH-ETR-v1.0.pdf <pdf/BE24.10-STIC_OPNSENSE_HIGH-ETR-v1.0.pdf>`          |
|          |                       | dfb3a7eceeace2302c8b7328602b959a9c3107c14395a591ddc08a704a8f0fdc                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| BE 24.04 | LINCE Compliant       | :download:`BE24.04-STIC_OPNSENSE_CQ-ETR-v1.0.pdf <pdf/BE24.04-STIC_OPNSENSE_CQ-ETR-v1.0.pdf>`              |
|          |                       | dd3a6aed7147ebfa64d4242a45001431e4de52d4faada6d5cdbbe0146bdd8790                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| BE 23.10 | LINCE Certified       | :download:`BE23.10-STIC_OPNSENSE_CQ-ETR-v1.0.pdf <pdf/BE23.10-STIC_OPNSENSE_CQ-ETR-v1.0.pdf>`              |
|          |                       | 3cd1135bee4c17299d4740c10ed9ef965b77be6e3899cc1c7587b9578930ea51                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| BE 23.04 | LINCE Compliant       | :download:`BR23.04-STIC_OPNSENSE_CQ-ETR-v3.1.pdf <pdf/BE23.04-STIC_OPNSENSE_CQ-ETR-v3.1.pdf>`              |
|          |                       | 9cce20526a25de2f03b29dcb80df8277eac4eb02066e504396c07e0caffd104e                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| BE 22.10 | LINCE Compliant       | :download:`BE22.10-STIC_OPNSENSE_CQ-ETR-v2.0.pdf <pdf/BE22.10-STIC_OPNSENSE_CQ-ETR-v2.0.pdf>`              |
|          |                       | 6fae801d18c3c8574ab8cca9a6f03f8b898dbe8a22136ee8fc8aa01173539fb4                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| BE 22.04 | LINCE Compliant       | :download:`BE22.04-STIC_OPNSENSE_CQ-ETR-v1.0.pdf <pdf/BE22.04-STIC_OPNSENSE_CQ-ETR-v1.0.pdf>`              |
|          |                       | 5b303285f3b9f9cd6290a623d7c509e48c59da4c678884a1513e84ee7d06d5d1                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+


External references
............................................................

* https://www.jtsec.es/product-security-testing

  -  `Standard definitions <https://www.jtsec.es/files/CCN-LINCE-001_v0.1_final_EN.pdf>`__
  -  `Evaluation methodology <https://www.jtsec.es/files/CCN-LINCE-002_v0.1_final_EN.pdf>`__

* https://www.ccn.cni.es/index.php/en/menu-ccn-en
* https://cpstic.ccn.cni.es/en/

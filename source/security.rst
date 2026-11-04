====================================
Security
====================================

.. contents:: Index


------------------------------------------------------------
Intro
------------------------------------------------------------

As a trusted open source security product, we do care a lot about security and, with our regular release schedule, we
try to stay ahead of possible incidents. Even though we are cautious and stay informed, sometimes issues
do occur, in which case it is good to know what to do.


------------------------------------------------------------
Staying ahead
------------------------------------------------------------

Even though we always encourage people to update regularly, sometimes it is not possible to do so for various reasons.

Luckily, OPNsense comes with an integrated security check for known vulnerabilities, which can be found in our firmware
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
    end as this often depends on features used and settings configured. Our advice always will be to upgrade into the
    latest community or business version.


.. Warning::

    Please do not report issues to us reported by the security health check, they are already known and highly likely
    a fix is pending for the next release.


------------------------------------------------------------
Assessing risks
------------------------------------------------------------

As with all software, understanding how software is being developed helps a lot assessing the risks involved when using with it.
Most software components are built on top of other components, which all have their own security challenges. From an architecture
perspective, we do try to minimize the external dependencies as much as possible, but obviously need various software components
for the broad spectrum of features that we offer.

When we add functionality ourselves (supported under :doc:`tiers 1 and 2 </support>`), we tend to ask ourselves at least the following questions:

* Does the new component we plan to add replace something we already use, and how are we going to make sure we don't end up with just one more component?

  * A good example of this is the use of `tabulator <https://www.tabulator.info/>`__ which gradually replaced bootgrid we used earlier

* How active is the development of the component in question, and what level of support can be expected?
* What is the expected maintenance burden, and is it reasonable in relation to the added functionality?

  * When a library offers minimal additional functionality compared to the tools already available in the language being used, it's often better to build and maintain the functionality ourselves to keep dependencies more manageable.
  * Also, when we already have a component offering almost the same functionality, does adding another one make sense?

* Could we [easily] replace a component with an alternative or maintain the software ourselves?

  * An example of this is our previous use of Phalcon to support most of our MVC code, which has since been largely rewritten using standard PHP code.


Although our development manual contains a lot of detail on how we work, it doesn't hurt to explain our approach here at a high level,
with more focus on its security aspects. Different components in the stack may take slightly different approaches to handling security issues.
While planning and building releases, all these topics are taken under consideration.


[FreeBSD] Base system and kernel
............................................................

Although we prefer to use release versions of our operating system software, the release cadence between OPNsense and FreeBSD
differs, which in practice means we start with a release version (e.g. :code:`15.1`) and track upstream security issues when
planning releases on our end. The FreeBSD advisories are publicly available [1]_. in case of doubt,
the ones we implemented are mentioned in our release notes [2]_. and recorded in our publicly available source repository [3]_.

.. [1] https://www.freebsd.org/security/advisories/
.. [2] https://docs.opnsense.org/releases.html
.. [3] https://github.com/opnsense/src


[ports] External software
............................................................

External software in most BSD's is managed via a "ports collection", which is more or less a recipe book describing
how to construct different pieces of software.  OPNsense hosts a (partial) mirror of the upstream collection with
some specific software additions on top for binary software we maintain ourselves.

In order to track vulnerabilities, one can use VuXML [4]_ ., which can also be queried directly from the OPNsense interface using
the "security audit" feature in the firmware section.

Although not all security incidents on software installed may have impact on your setup, this information offers insights
into the risks involved with your running configuration.

Below an example of a report extracted via the audit feature.

.. code-block:: text
   :linenos:

    python313-3.13.15 is vulnerable:
      Python -- poplib module, when passed a user-controlled command, can have additional commands injected using newlines
      CVE: CVE-2025-15367
      WWW: https://vuxml.FreeBSD.org/freebsd/6d3488ae-2e0f-11f1-88c7-00a098b42aeb.html

The first line (1) explains which software package the jeopardy refers to, next (2) there are some details about the incident which
helps assessing if this particular issue impacts you, when one or more CVE's are attached you can find them in the following lines (3),
followed by a link to more information (4).

When planning releases, we use the same information to determine impact on our product.


.. [4] https://vuxml.freebsd.org/freebsd/index.html


[tier 1 & 2 software] OPNsense
............................................................

As mentioned further below, security incidents in our software can be reported via our GitHub tracker [5]_ in which
case users can be informed and optionally, depending on the type of problem, a CVE may be assigned.

We work closely with security researchers around the world to identify and address issues that may have slipped into our software,
just as we do with the software we use.

These days, we tend to use this tracker as our primary source of communication when it comes to security-relevant issues.

Our release notes [6]_ also refer to these fixes.


.. [5] https://github.com/opnsense/core/security/advisories?state=published
.. [6] https://docs.opnsense.org/releases.html


------------------------------------------------------------
Upstream vulnerabilities
------------------------------------------------------------

Since OPNsense is a collection of open source software, when finding an issue, it is always a good idea to
inspect where it should be fixed first. In case you do not know or are not sure, you can still ask on our end, just
know that we do not have the manpower to act as an intermediary between various projects.


.. _security-deployment-considerations:

------------------------------------------------------------
Deployment considerations
------------------------------------------------------------

A firewall is a security tool and should be deployed and operated accordingly.
While OPNsense provides mechanisms to help secure a network environment,
no firewall can compensate for weak operational practices or excessive trust relationships.

Users who are granted access to the firewall typically perform administrative or operational tasks and therefore
require an elevated level of trust.
Administrative access should be limited to users who require it for their role, and permissions should be assigned according
to the principle of least privilege whenever possible.

.. admonition:: Trusted administrators only


  Some access control roles provide capabilities that effectively allow complete control over the system, either directly or indirectly,
  and should therefore only be assigned to fully trusted administrators or administrative peers.

  In particular, these privileges should only be assigned to users trusted with full administrative control:

  * ``System: Wizard`` can change the root password, including after the initial setup has been completed.
  * ``System: Configuration: Backups`` can export sensitive configuration and restore configuration that replaces
    administrator credentials and other security settings.
  Neither privilege is suitable for a limited administrator, even if the user does not have separate user-management
  privileges. ``XMLRPC Library`` can be used for remote configuration synchronisation and automation.
  Other access to configuration data, remote management interfaces, backup material or automation mechanisms should
  also be considered security-sensitive and assigned with care.


.. admonition:: Fine-grained permissions and trust

  Access control lists can provide fine-grained permissions for operational convenience, delegation and improved visibility.
  Depending on the use case, these permissions may also serve as effective security boundaries.

  Administrators should, however, consider the effective capabilities granted by a role rather than relying solely on the apparent scope of individual privileges.
  Some permissions may appear limited in scope while still allowing users to influence or bypass related security controls indirectly.

  For example, a user who is permitted to manage port forwarding rules may be able to create access paths to systems or services that would otherwise remain inaccessible.

  Permission assignments should therefore reflect both the intended task and the level of trust placed in the user receiving them.


.. admonition:: Legacy components

  Some legacy components, identified by URIs ending in ``.php``, originate from earlier parts of the codebase and may implement
  fewer validation and access control safeguards than newer components.
  Access to these pages should therefore be restricted to fully trusted administrators whenever possible.


Access to the management interface should be restricted to trusted networks and secured using strong authentication mechanisms.
Administrative accounts should use unique passwords and additional authentication factors where supported and appropriate.

To reduce the attack surface, unnecessary services, plugins and user accounts should be disabled or removed.
Systems should be kept up to date by installing security and maintenance updates in a timely manner.

Regular reviews of firewall rules, user accounts, exposed services and remote access methods help ensure that configurations
continue to reflect operational requirements and do not unintentionally introduce security risks.

Configuration backups should be created regularly and stored securely to facilitate recovery from hardware failures,
configuration errors or security incidents.
Logging and monitoring should be enabled to assist with troubleshooting, auditing and the detection of unexpected behaviour.

Security is not a single configuration option or deployment step, but an ongoing process of review,
maintenance and adaptation to changing requirements and threats.

------------------------------------------------------------
Reporting an incident
------------------------------------------------------------

Security incidents on our product can be reported using our `GitHub repository <https://github.com/opnsense/core/security>`__.
You may also create a new issue and select "Report a security vulnerability", which will redirect you to the same page.
Alternatively, you can report security issues to our security team available at **security** @ **opnsense.org**.

All reports should contain at least the following information:

* A clear description of the vulnerability at hand
* Which versions of our product seem to be affected
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

Within the OPNsense team and community, we spend a lot of time safeguarding our software and keeping up with the latest threats,
like checking used software against CVEs on every release, implementing best practices in our development methods and
offering clear and transparent release engineering.

To improve this even further, we decided to bring a third party on board and mold a process around our security verification
by trained security professionals.


Business Edition
............................................................

As our Business Edition is aimed at professional users, it does make sense to offer additional safeguards, like even more extensive testing on
this product. Looking at the lifecycle of our software, this is also the most mature stage of what we do have to offer:

* Development version

  -  Available at every release, it offers a glimpse of what to expect in the near future.

* Community version

  - When changes survive the development version, these are included in the community version, these are internally tested and
    feedback has been offered by community members.

* Business Edition

  - Functional changes are being included in a more conservative manner, more feedback has been collected from development
    and community, leading to a mission-critical version of the well-known OPNsense firewall.

As security testing is quite time-consuming, we aim to offer a full qualification cycle for every major release.


Framework / Type of testing (LINCE)
............................................................

In our quest for a framework to use, we found the LINCE methodology.

LINCE is a lightweight methodology for evaluating and certifying ICT products, created by Spain's National Cryptologic Center (`CCN <https://cpstic.ccn.cni.es/en/>`__),
based on Common Criteria principles and oriented around vulnerability analysis and penetration tests.

LINCE's strengths over other methodologies mainly consist of reduced effort and duration.
However, the way in which it is applied also makes it possible to pay more attention to the critical points of each product,
giving more weight to concrete and practical tests that combat real threats than to dense documentation or exhaustive functionality tests.

As most frameworks are not intended to be repeated very regularly, together with `jtsec <https://www.jtsec.es/>`__ we came up with an approach which
makes it possible to pass the test twice a year, which is needed to align with our Business Edition releases.

During every cycle, there is always a chance that (small) issues appear which should be fixed, in close accordance with jtsec, the OPNsense
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

The certification steps are executed twice a year, once for each Business Edition release. This process is quite time consuming, but
adds another independent party to the mix.

Timeline
............................................................
The first fully certified product has been a community version (21.7.1), which offered us insights into the process and
helped us improve the process which we would like to use for the Business Edition. We started this cycle with version 22.4
including full testing by jtsec.

Results
............................................................

Below you will find the versions that have been tested or are currently in testing.


+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| Version  | Status                | Download                                                                                                   |
+==========+=======================+============================================================================================================+
| BE 26.04 | LINCE Certified       | :download:`BE26.4-STIC_OPNSENSE_IAD-2604-ETR-v1.0.pdf <pdf/BE26.4-STIC_OPNSENSE_IAD-2604-ETR-v1.0.pdf>`    |
|          |                       | 20a376e76c55fbb555ed788b0df6466a48eafdcfb9305ef956138c410648f9ac                                           |
+----------+-----------------------+------------------------------------------------------------------------------------------------------------+
| BE 25.10 | LINCE Certified       | :download:`BE25.10-OPNSENSE_IAD-2510_v1.0.pdf <pdf/BE25.10-OPNSENSE_IAD-2510_v1.0.pdf>`                    |
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

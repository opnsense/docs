==============
Log Files
==============

When troubleshooting problems with your firewall, it is very likely you have to check
the logs available on your system. In the UI of OPNsense, the log files are generally grouped
with the settings of the component they belong to. The log files can be found here:

================ ======================================================== =============================================================================
 **Live View**    :menuselection:`Firewall --> Log Files --> Live View`    *View firewall logs in realtime, smart filtering can be applied*
 **Plain View**   :menuselection:`Firewall --> Log Files --> Plain View`   *Just the plain contents how* **pf** *logs into* **filter.log**
================ ======================================================== =============================================================================

Live View
---------

Live view updates itself in realtime if a rule is matched that has logging enabled or one of the global logging options is enabled under:
:menuselection:`System --> Settings --> Logging`

In the top left corner of the page you can build filter conditions for rules to match when inspecting traffic, while
here you can select different fields (for example `label`, `src` address, `dst` address) and how to match them
(contains, is, is not, does not contain) combined with a criteria (either a string or a preselected value, depending on type).
The [+] button adds the the filter to the view.

By default results should match all criteria (AND), but you can change that to an any of criteria (OR). The latter is sometimes
practical if you want to track a small list of hosts.

Detailed information for a specific rule can be provided using the info button at the end of each line.

.. Tip::

  The :code:`host` and :code:`port` fields are a bit special and apply to both source and destination, which makes sure that
  traffic matched to and from a specific address or port are both matched.

.. Tip::

  Usually a rule contains a :code:`rid` field which corresponds to the rule or setting in OPNsense responsible for this match,
  when clicking on the link the system will try to redirect you to the correct setting (or rule).

.. Note::

    The live log only shows rules that are matched by the firewall, in case a state is created the flow will be reported for the first packet,
    as long as the state still exists no new lines will be reported for the same traffic flow.
    If you need to inspect raw traffic, it's often practical to combine the live-log with the packet capture feature found under
    interface diagnostics in the menu.

.. Note::

    Since log lines are stored on the system without an exact match to the rule in question, we do need to translate the sequence
    in the file back to the rule definition stored in the system. Due to this fact, the information is less accurate
    historically if the firewall was reconfigured. (labels may be incorrect when looking at older data)

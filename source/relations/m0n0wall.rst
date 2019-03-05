========
M0n0wall
========

.. image:: ./images/index.png

----------
Background
----------

*Manuel Kasper*

::

  Ever since I started playing with packet filters on embedded PCs, I wanted to
  have a nice web-based GUI to control all aspects of my firewall without having
  to type a single shell command.

  There are numerous efforts to create nice firewall packages with web
  interfaces on the Internet (most of them Linux based), but none met all my
  requirements (free, fast, simple, clean and with all the features I need).
  So, I eventually started writing my own web GUI. But soon I figured out that
  I didn't want to create another incarnation of webmin – I wanted to create a
  complete, new embedded firewall software package.

  It all evolved to the point where one could plug in the box, set the LAN IP
  address via the serial console, log into the web interface and set it up.

  Then I decided that I didn't like the usual bootup system configuration with
  shell scripts (I already had to write a C program to generate the filter rules
  since that's almost impossible in a shell script), and since my web interface
  was based on PHP, it didn't take me long to figure out that I might use PHP
  for the system configuration as well.

  That way, the configuration data would no longer have to be stored in text
  files that can be parsed in a shell script – it could now be stored in an XML
  file. So I completely rewrote the whole system again, not changing much in the
  look-and-feel, but quite a lot "under the hood".


---------------------------
End of the m0n0wall project
---------------------------
The active development of m0n0wall ended in 2015.

Manuel Kasper, wrote the following on 15 February 2015:

::

  Dear m0n0wall enthusiasts,

  on this day 12 years ago, I have released the first version of m0n0wall to
  the public. In theory, one could still run that version - pb1 it was called -
  on a suitably old PC and use it to control the Internet access of a small LAN
  (not that it would be recommended security-wise). However, the world keeps
  turning, and while m0n0wall has made an effort to keep up, there are now better
  solutions available and under active development.

  Therefore, today I announce that the m0n0wall project has officially ended.
  No development will be done anymore, and there will be no further releases.

  The forums and the mailing list will be frozen at the end of this month.
  All the contents of the website, repository, downloads, mailing list and forum
  will be archived in a permanent location on the web so that they remain
  accessible indefinitely to anyone who might be interested in them.

  m0n0wall has served as the seed for several other well known open source
  projects, like pfSense, FreeNAS and AskoziaPBX.

  The newest offspring, OPNsense (https://opnsense.org), aims to continue the open source spirit of
  m0n0wall while updating the technology to be ready for the future. In my view,
  it is the perfect way to bring the m0n0wall idea into 2015, and I encourage all
  current m0n0wall users to check out OPNsense and contribute if they can.

  Finally, I would like to take this opportunity to thank everyone who has been
  involved in the m0n0wall project and helped in some way or another -
  by contributing code, documentation, answering questions on the mailing
  list or the forum, donating or just spreading the word. It has been a great
  journey for me, and I'm convinced that even now that it has come to an end,
  the m0n0wall spirit will live on in the various projects it has spawned.


-----------------------
Relations with OPNsense
-----------------------

Deciso B.V. the founder of OPNsense has taken over the m0n0wall websites from
Manuel Kasper and continues to offer all the sources, website & forum content
both as a historical reference as well as to preserve knowledge gained.

The OPNsense core team would like to thank Manuel for all his efforts, as without
him OPNsense would not have been possible.

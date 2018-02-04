====================
Development Workflow
====================

.. image:: images/flow.png

It’s pretty hard to approach a larger repository you have never
worked with. The biggest issue is that few projects have defined
development (as in actual coding) workflow laid out for new
contributors, so one is just going to be stabbing in the dark for a few
days or weeks until things start making sense. Speaking of *sense*,
let’s explain how we’ve designed the development experience for
`OPNsense <https://opnsense.org/developers-invitation/>`__ and how you
can start contributing code in no time.

---------
Structure
---------

.. rubric:: Source, Ports, Core, Tools
   :name: structure-source-ports-core-tools

The structure is pretty much FreeBSD: we have a `source
code <https://github.com/opnsense/src>`__ repository and a `ports
tree <https://github.com/opnsense/ports>`__. Historically, we also have
a `core code <https://github.com/opnsense/core>`__ and `tools
repository <https://github.com/opnsense/tools>`__. The tools repository
is project shell code gluing all repositories together, producing final
images, while the core is the important GUI and system configuration
bits.

.. Note::

  As of 16.1 there is also plugin support, the source repository is `plugins tree <https://github.com/opnsense/plugins>`__ .
  Plugins are a modular way of easily extending the existing system.

.. rubric:: Why core is not a part of source
   :name: core-not-part-of-source

The first thing that’s interesting is that the core is not part of
the source repository, because it depends on third party software found in the
ports. We can’t stick core into source, because ports are things that
don’t fit into the base system. It also helps to keep source repository
changes to the minimum to make major FreeBSD upgrades easier in the
future.

.. rubric:: Why core isn't part of ports either
   :name: core-not-part-of-ports

Why is the core repository not in the ports? Well, we have a couple of
custom ports in the ports tree, but these are small. The core repository as
well as the ports tree itself are so big that it made sense to keep them
separate. Another reason is that the core repository only contains scripts in
Shell, Python and PHP. So the tools repository actually treats the core
repository as a package that depends on all the ports it needs. This
way, on the images, it looks like the core code is just another package.
**That makes upgrading the core code very easy and fast without modifying
base.** We can even upgrade to newer ports pages and add and remove them
as we go forward.

--------
Building
--------
.. rubric:: Not Clobbering the Build System
   :name: building-not-clobbering-the-build-system

The tools repository is designed to run on a stock FreeBSD using `chroot
mechanics <http://en.wikipedia.org/wiki/Chroot>`__ to keep the build
contained and consistent. There’s nothing worse than a build system that
modifies the build system and at some point starts to dash out working
images–only to stop working some time in the future. No, no, no.

You can also “cross-build” between FreeBSD versions. We’ve successfully
built images on FreeBSD 10.1 when OPNsense was still running on FreeBSD 10.0.
(version 16.1 now runs on FreeBSD 10.2) That’s not a huge gap and the ABI is the
same, but we expect this to work with FreeBSD 11 and beyond as well so that if
you have a FreeBSD box you will always be able to produce your own images if you
desire–without spinning up extra machines, jails or virtual machines.

Here are the `build instructions for
OPNsense <https://github.com/opnsense/tools/blob/master/README.md>`__.

.. TIP::

  As of November 2015 OPNsense is equipped with a tool that can completely
  reinstall a running system in place for a thorough factory reset or to restore
  consistency of all the OPNsense files. It can also wipe the configuration
  directory, but won't do that by default.
  The `opnsense-bootstrap <https://github.com/opnsense/update>`__ script is
  particularly useful if you want to convert a hosted FreeBSD system to OPNsense.

-------------------------------
Virtual Machine for Development
-------------------------------

.. rubric:: Running: Use a Virtual Machine for Development
   :name: running-use-a-virtual-machine-for-development

It’s just easier and less tedious if the kernel crashes, to revert to a
previous state, or isolate and test different features. A VM can be set
up easily using the ISO images. Also very good for testing installation
and upgrades. Of course, at some point you will want to bring OPNsense
to your actual target device—just make sure you know the system well
enough before you attempt this.

`VirtualBox <https://www.virtualbox.org/>`__ is a solid tool for the
job, but be sure to check out `FreeBSD’s Bhyve <http://bhyve.org/>`__ as
well (it was added in FreeBSD 10.0). However, If you are only interested
in GUI coding, you can skip all the build parts and directly download an
image and spin it up. Because…

--------
Packages
--------

.. rubric:: It Gets Even Better
   :name: packages-it-gets-even-better

Once you have a running instance, how to produce and push code? Well,
there’s a couple optional of packages that help you to be productive:

::

    # pkg install vim-lite joe nano gnu-watch git tmux screen

The most important one is *git* for obtaining the code, the rest is
optional if you need it—mostly editors and terminal wrappers. It is also
possible to mount sshfs or do sftp to sync files from the repo if you
would like to use a graphical editor from your own system. As the root
user do the following:

::

    # cd
    # git clone https://github.com/opnsense/core

Once you have the repository, you switch it live using:

::

    # cd core
    # make mount

Yes, the changes that you make in the repository will show up directly
in the GUI now! Unfortunately, this will mount the repo over
*/usr/local* so if you modify packages the changes will light up in git.
Be careful. To prevent that from happening you can temporarily unmount
using:

::

    # make umount

To finish that off the boot sequence will mount the core repository set
up in */root/core* as early as possible (if it’s available) and will use
its modifications for booting up (with the exception of
/usr/local/etc/rc itself). This makes it possible to work on the backend
configuration and boot sequence improvements without having out of sync
system files and repositories.

-------
Summary
-------

.. rubric:: Easy Access is Key to Collaboration
   :name: summary-easy-access-is-key-to-collaboration

Although this is just a peek into OPNsense development workflow it brings to
attention a key aspect: moving barriers out of the way to enable as many people
as possible to produce quick results. Yes,there are barriers like
`git <http://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>`__
and `GitHub <https://guides.github.com/activities/contributing-to-open-source/>`__
to deal with, maybe even learning FreeBSD intricacies, but once you have
your code in the GUI and working fine, you’ll feel proud enough to
endure the hardships of making sure your patch will have a place in our
upstream repositories so the community as a whole can benefit from your
dedication.

The OPNsense core team looks forward to your feedback;
"We are seeking for more improvements in the build system and eagerly await
your pull requests." Take care and code responsibly. :)

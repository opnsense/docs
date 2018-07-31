=============================
Installing OPNsense AWS image
=============================
.. image:: images/amazon-web-services.png
    :width: 100%

To apply for access to the OPNsense Amazon AWS EC2 cloud image, you need:

* An active support subscription
    see: https://opnsense.org/support-overview/commercial-support/)
* Supply your Amazon Account Number
    to share the Amazon Machine Image with.

---------------------
Step 1 - New Instance
---------------------
Start a new instance and then go to "instances", followed by "launch instance"
and then "My AMIs", don't forget to select "Shared with me"


--------------------
Step 2 - Select Type
--------------------
Choose an instance type

.. image:: images/aws_launch_new_image.png
    :width: 100%

---------------------------------
Step 3 - Configure security group
---------------------------------
To configure security group, make sure you allow https access from your own network.

.. image:: images/aws_configure_security_group.png
    :width: 100%


-------------------------
Step 4 - Configure a disk
-------------------------

.. image:: images/aws_choose_disc.png
    :width: 100%


-----------------------------
Step 5 - Review your settings
-----------------------------

.. image:: images/aws_review_settings.png
    :width: 100%

--------------------
Step 6 - SSH keypair
--------------------
Select ssh keypair or skip, the ssh key isn’t used for OPNsense, ssh is disabled by default.

.. image:: images/aws_ssh_keypair.png
    :width: 100%

---------------------------
Step 7 - Review status page
---------------------------

.. image:: images/aws_status.png
    :width: 100%

----------------------
Step 8 - AWS instances
----------------------
Go to your AWS instances

.. image:: images/aws_instances.png
    :width: 100%

Select the image, go to “image settings” then “get system log” to obtain the
initial password

------------------------------
Step 9 - Initial root password
------------------------------
Copy your initial root password (line ** set initial….)

.. image:: images/aws_capture_initial_password.png
    :width: 100%

--------------------------------
Step 10 - Search current address
--------------------------------

.. image:: images/aws_search_current_ip.png
    :width: 100%


Login to OPNsense using the address provided.

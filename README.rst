========================
``gs.group.member.info``
========================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Group membership information viewlets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-19
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.


Introduction
============

This product contains some viewlets_ that display the group membership
information.

Viewlets
========

Two viewlets display membership information on the group page [#home]_:

* `Logged-in member`_ and
* `Public group`_.

The `Administration Links`_ are defined here for want of a better place.

Logged-In Member
----------------

Logged-in group members see a viewlet that contains three items of
information:

#. The visitor is a member,
#. The visitor can leave the group, and
#. A link to change the email settings for the group.

The *Leave* link is quite prominent, because the alternative is to have the
group-member mark the group as spam.

Public Group
------------

The public-group viewlet is shown to members of the general public who are
looking at a group (which may be either a public or a private group).

* In all cases a *login* link shown, in case the visitor is a group member.
* If the group is public then a *register* link is shown.
* If the group is private then a *request membership* link is shown.

The *login* link is given prominence, because it is a pain when a
registered member try and sign up for a group that he or she is already a
member of.

Administration Links
--------------------

The administration links are an unordered-list of links (``<ul>``) that a
site administrator or a group administrator can use [#site]_. A viewlet
supplies a list item (``<li>``) by adding itself to the
``gs.group.member.info.interfaces.IGroupMemberAdminLink`` manger::

  <browser:viewlet
    name="gs-group-member-invite-home-admin"
    manager="gs.group.member.info.interfaces.IGroupMemberAdminLinks"
    template="browser/templates/admin_list.pt"
    class="gs.group.member.viewlet.GroupAdminViewlet"
    permission="zope2.ManageUsers"
    weight="10"
    title="Invite Members" />

The viewlet manager is provided here because every single link is to do
with member management.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.member.info
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#home] See ``gs.group.home``
           <https://source.iopen.net/groupserver/gs.group.home>
.. [#site] The viewlet manager for the links that only a site administrator
           can use are provided by the ``gs.group.properties`` product
           <https://source.iopen.net/groupserver/gs.group.product>

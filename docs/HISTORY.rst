Changelog
=========

4.1.1 (2015-02-27)
------------------

* Added internationalisation support
* Added integration with Transifex_
* Switching to GitHub_ as the primary code repository

.. _Transifex:
   https://www.transifex.com/projects/p/gs-group-member-info/
.. _GitHub: https://github.com/groupserver/gs.group.member.info/

4.1.0 (2014-03-25)
------------------

* Adding the restricted-group viewlet

4.0.3 (2013-10-18)
------------------

* Switching to full URLs so the zope.schema.URI field accepts the
  input

4.0.2 (2013-06-13)
------------------

* Adding the ``gs-group-member-info`` class to the viewlet page
  templates
* Updating the navigation links for a logged-in member

4.0.1 (2013-04-23)
------------------

* Updating the icons in the *Join* button, *Register* button, and
  *Sign in* button.

4.0.0 (2013-03-19)
------------------

* Moving the viewlets to `gs.group.member.viewlet`_
* Moving the utility functions to `gs.group.member.base`_

.. _gs.group.member.viewlet:
   https://github.com/groupserver/gs.group.member.viewlet/
.. _gs.group.member.base:
   https://github.com/groupserver/gs.group.member.base/

3.0.1 (2013-02-20)
------------------

* Adding some WAI-ARIA roles

3.0.0 (2013-02-11)
------------------

* Adding the *Membership* viewlet to the *Group* page
* Adding a new *Members administration* viewlet manager and
  viewlet

2.1.1 (2012-09-27)
------------------

* Importing the viewlets into the ``__init__`` for the product

2.1.0 (2011-07-14)
------------------

* Making ``user_member_of_group`` more flexible with its input
* Adding the participation coach check to the utility functions
* Fixing a return value

2.0.0 (2011-05-23)
------------------

* Adding the viewlet classes from `gs.group.base`_ and
  `gs.group.home`_
* Adding the ``MemberViewlet``

.. _gs.group.base: https://github.com/groupserver/gs.group.base/
.. _gs.group.home: https://github.com/groupserver/gs.group.home/


1.1.0 (2011-04-15)
------------------

* Adding some more utility functions

1.0.0 (2010-07-28)
------------------

Initial version. Prior to the creation of this product the group
membership information was mostly provided by the
``Products.GSGroupMember`` product.

..  LocalWords:  Changelog Transifex GitHub

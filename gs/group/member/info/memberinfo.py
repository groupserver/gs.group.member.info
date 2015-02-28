# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from gs.group.privacy import GroupVisibility
from gs.group.member.viewlet import MemberViewlet


class MemberInfo(MemberViewlet):

    def __init__(self, group, request, view, manager):
        super(MemberInfo, self).__init__(group, request, view, manager)

    @Lazy
    def groupVisibility(self):
        retval = GroupVisibility(self.groupInfo)
        return retval


class LoggedInMemberInfo(MemberInfo):
    '''Membership information for logged in members'''
    @Lazy
    def show(self):
        retval = self.isMember
        return retval


class PublicGroupMemberInfo(MemberInfo):
    '''Membership information (joining) for public groups.'''
    @Lazy
    def show(self):
        retval = not(self.isMember) and self.groupVisibility.isPublic
        return retval


class RestrictedGroupMemberInfo(MemberInfo):
    '''Membership information (joining) for restricted groups.'''
    @Lazy
    def show(self):
        retval = not(self.isMember) and self.groupVisibility.isPublicToSite
        return retval


class PrivateGroupMemberInfo(MemberInfo):
    '''Membership information (joining) for private groups'''
    @Lazy
    def show(self):
        retval = not(self.isMember) and self.groupVisibility.isPrivate
        return retval


# Secret groups are only shown to group members, so there is no joining
# information.

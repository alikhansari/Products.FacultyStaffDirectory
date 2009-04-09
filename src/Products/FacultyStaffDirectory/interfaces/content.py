# -*- coding: utf-8 -*-
"""Interfaces for content types (and a tool)"""
# TODO: Stick methods or at least docstrings describing the contracts on these!

__author__ = """WebLion <support@weblion.psu.edu>"""
__docformat__ = 'plaintext'

from zope.interface import Interface

class IPersonGrouping(Interface):
    """A grouping of person objects"""

    def getPeople():
        """Return a list of people."""

    def getSortedPeople():
        """Return a sorted list of people."""

class IClassification(IPersonGrouping):
    """A classification"""

class IDepartment(IPersonGrouping):
    """A department"""

class ISpecialty(IPersonGrouping):
    """An academic specialty"""

class ICommittee(IPersonGrouping):
    """A committee"""
    
class ICommitteeMembership(Interface):
    """A committee membership"""

class ICommitteesFolder(Interface):
    """A committees folder"""

class ICourse(Interface):
    """A course"""

class IDepartmentalMembership(Interface):
    """A departmental membership"""

class IFacultyStaffDirectory(Interface):
    """A FacultyStaffDirectory."""
                               
class IFacultyStaffDirectoryAddable(Interface):
    """A content type to be set as an addable_type within a FacultyStaffDirectory."""

class IPerson(Interface):
    """A person"""
                               
class ISpecialtiesFolder(Interface):
    """An academic specialties folder"""

class ISpecialtyInformation(Interface):
    """information about an association of a specialty to a person"""

class IFacultyStaffDirectoryTool(Interface):
    """The FacultyStaffDirectory tool"""
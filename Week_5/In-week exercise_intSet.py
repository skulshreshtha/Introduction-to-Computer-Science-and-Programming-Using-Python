# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 07:05:00 2019

@author: Shobhit Kulshreshtha
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def __len__(self):
        """Returns the number of elements in self"""
        count = 0
        for e in self.vals:
            count +=1
        return count
        
    def intersect(self, other):
        """ Returns the common elements between self and other intSet"""
        assert type(self) == type(other)
        common = intSet()
        for e in self.vals:
            if other.member(e):
                common.insert(e)
        return common         

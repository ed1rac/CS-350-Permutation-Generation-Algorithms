import pytest
from unittest import TestCase

from pytest import list_of

from sjt import sjt
from heaps import heaps
from itertools import permutations

def stdLibPerms(l):
  return [list(i) for i in permutations(l)] #permutations returns a list of tuples so I'm converting it to a list of lists

def comparePerms(p1, p2):
  found = False

  for i in p1:
    for j in p2:
      if sorted(i) == sorted(j):
        found = True
        break

    if found == False:
      return False
    else: 
      found == False

  return True

t = TestCase("__str__") #assertTrue is a method of TestCase, so to get to it I'm gonna just create a throw away instance of TestCase

@pytest.mark.randomize(l=list_of(int, min_items=0, max_items=6), ncalls=10)
def test_heaps(l):
  t.assertTrue(comparePerms(heaps(l), stdLibPerms(l)))

@pytest.mark.randomize(l=list_of(int, min_items=0, max_items=6), ncalls=10)
def test_sjt(l):
  t.assertTrue(comparePerms(sjt(sorted(l)), stdLibPerms(l)))


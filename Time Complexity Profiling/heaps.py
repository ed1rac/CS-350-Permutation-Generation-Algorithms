import cProfile
from copy import deepcopy

def heaps(set, time=False):
  def innerHeaps(n, set, perms=[]):
    #if zeroCheck(n):
      #return perms
    if oneCheck(n):
      perms.append(deepcopy(set))
      return perms
    else:
      for i in range(n):
        innerHeaps(n-1, set)
        j = 0 # extra assign; ignore this
        if oddCheck(n): #odd number
          assign(j, 0) #j = 0
        else:
          assign(j, i) #j = i
        swap(j, n - 1, set) #set[j], set[n-1] = set[n-1], set[j] #swap

    return perms

  if time:
    #profile in context because of inner function
    return cProfile.runctx('innerHeaps(len(set), set)', None, locals())
  else:
    return innerHeaps(len(set), set)

def swap(i, j, set):
  set[j], set[i] = set[i], set[j]

def oddCheck(n):
  return n % 2 == 1

def zeroCheck(n):
  return n == 0

def oneCheck(n):
  return n == 1

def assign(dest, src):
  dest = src

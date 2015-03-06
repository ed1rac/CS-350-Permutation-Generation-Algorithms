import cProfile
from copy import deepcopy

def heaps(set, time=False):
  def innerHeaps(n, set, perms=[]):
    if n == 0:
      return perms
    elif n == 1:
      perms.append(deepcopy(set))
      return perms
    else:
      for i in range(n):
        innerHeaps(n-1, set)
        if n % 2 == 1: #odd number
          j = 0
        else:
          j = i
        set[j], set[n-1] = set[n-1], set[j] #swap

    return perms

  if time:
    #profile in context because of inner function
    return cProfile.runctx('innerHeaps(len(set), set)', None, locals())
  else:
    return innerHeaps(len(set), set)

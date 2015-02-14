import cProfile

def heaps(set, time=False):
  def innerHeaps(n, set):
    if n == 1:
      print set
    else:
      for i in range(n):
        innerHeaps(n-1, set)
        if n % 2 == 1: #odd number
          j = 0
        else:
          j = i
        set[j], set[n-1] = set[n-1], set[j] #swap

  if time:
    #profile in context because of inner function
    cProfile.runctx('innerHeaps(len(set), set)', None, locals())
  else:
    innerHeaps(len(set), set)

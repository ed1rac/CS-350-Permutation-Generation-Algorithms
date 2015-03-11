import heaps
import sjt

def heapTests(lowerbound, upperbound, count):
  for i in range(lowerbound, upperbound + 1):
    for j in range(count):
      heaps.heaps(range(i), True)

def sjtTests(lowerbound, upperbound, count):
  for i in range(lowerbound, upperbound + 1):
    for j in range(count):
      sjt.sjt(range(i), True)

def grabtimes(location):
  f = open(location, 'r')
  for line in f:
    if 'function calls' in line:
      print(line)

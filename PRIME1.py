#@author:jubinchheda
#SPOJ: http://www.spoj.com/problems/PRIME1/
# First attempt

import sys
from sys import stdin
import fileinput

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  if n%5 == 0: return False
  if n%7 == 0: return False
  if n%11 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


   

paramList = []
stringList =[]

for line in fileinput.input():
   stringList.append(line.rstrip())
   
del stringList[0]

for item in stringList:
   paramList.append(item.split())
   
for item in paramList:
   low = int(item[0])
   high = int(item[1])
   for n in xrange(low, high+1):
      if(is_prime(n)):
	     print n
   print
   
	 

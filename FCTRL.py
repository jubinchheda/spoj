
import fileinput

def Z(n):
   p = 5
   result = 0
   while n>p: 
      result+=(n/p)
      p*=5
   print result


def inputToList(stringList):
   for line in fileinput.input():
      stringList.append(line.rstrip())
   return stringList
   
   
stringList = []
inputToList(stringList)
stringList.pop(0)
paramList = []
for item in stringList:
   paramList.append(item)
   
for item in paramList:
   Z(int(item))

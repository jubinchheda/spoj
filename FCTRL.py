import fileinput

def Z(n):
   p = 5
   result = 0
   while n>p: 
      result+=(n/p)
      p*=5
   return result


def inputToList(stringList):
   for line in fileinput.input():
      stringList.append(line.rstrip())
   return stringList
   
   
stringList = []
inputToList(stringList)
stringList.pop(0)

for item in stringList:
   print Z(int(item))

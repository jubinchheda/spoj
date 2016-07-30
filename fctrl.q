In trying to answer [SPOJ Question FCTRL][1], which effectively asks that given a number, find the number of trailing zero's. I tried several test cases and the code seems fine to me but the online judge seems to be rejecting my submission as wrong answer. Any suggestions on a fix are much appreciated. Any other pointers on coding style, etc also very welcome. `import fileinput

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
   print Z(int(item))`

Code is available on [github][2]


  [1]: http://www.spoj.com/problems/FCTRL/
  [2]: https://github.com/jubinchheda/spoj/blob/master/FCTRL.py

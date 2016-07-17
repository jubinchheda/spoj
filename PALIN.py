#@author:jubinchheda
#SPOJ: http://www.spoj.com/problems/PALIN

#import sys
import fileinput

def is_pal(s):
   return s == s[::-1]
	
def printNextPal(n):
   while(True):
      n = n + 1
      #print n
      if(is_pal(str(n))):
         print n
         return		 
   return
   
def returnMirrored(str1, pivot, leng):
   #print str1
   res = str1[:leng-pivot]
   #	print res
   #print res
   #str1List = list(str1)
   #print str1List
   rev = str1[::-1]
   if(leng%2==1):
      pivot=pivot+1
   res = res + rev[pivot:]
   #print res
   #if)
   return res
   
   
def printNextPal2(n):
   #while(true):
   n = n +1
   if(is_pal(str(n))):
      print n
      return
   strN = str(n)
   leng = len(strN)
   strTest = returnMirrored(strN, leng/2, leng)
   cand = int(strTest)
   if cand >= n:
      print cand
   else:
      halfLen = leng/2
      powTen = 10**halfLen
      n = n + powTen
      strN = str(n)
      leng = len(strN)
      strTest = returnMirrored(strN, leng/2, leng)
      print strTest
      
	


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
   
#print paramList
for item in paramList:
   #printNextPal(int(item))
   printNextPal2(int(item))

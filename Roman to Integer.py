from unittest import result


class Solution(object):
   def romanToInt(self, s):
      """
      :type s: str
      :rtype: int
      """
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
      i = 0
      num = 0
      while i < len(s):
            #print(i)
            num+=roman[s[i]]
            i+=1
      return num
ob1 = Solution()
#print("result")
print(ob1.romanToInt("CDXLIII"))
#print(ob1.romanToInt("CDXLIII"))
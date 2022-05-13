"""
Question:

Have the function PalindromeCreator(str) take the str parameter being passed and determine if it is possible to create a palindromic string of minimum length 3 characters by removing 1 or 2 characters. 
For example: if str is "abjchba" then you can remove the characters jc to produce "abhba" which is a palindrome. 
For this example your program should return the two characters that were removed with no delimiter and in the order they appear in the string, so jc. 
If 1 or 2 characters cannot be removed to produce a palindrome, then return the string not possible.
If the input string is already a palindrome, your program should return the string palindrome. 
Your program should always remove the characters that appear earlier in the string. 
In the example above, you can also remove ch to form a palindrome but jc appears first, so the correct answer is jc.
The input will only contain lowercase alphabetic characters. 
Your program should always attempt to create the longest palindromic substring by removing 1 or 2 characters (see second sample test case as an example). 
The 2 characters you remove do not have to be adjacent in the string. 

"""

def PalindromeCreator(strParam):

  if strParam == strParam[::-1]:
    return "palindrome"
  
  a = strParam

  for i in range(len(strParam)):
    b = a.replace(a[i],"")
    if b == b[::-1] and len(b)>2:
      return a[i]
  
  for i in range(len(strParam)):
    b = a.replace(a[i],"")
    for j in range(i,len(b)):
      c = b.replace(b[j],"")
      if c==c[::-1] and len(c)>2:
        return a[i]+b[j]

  return "not possible"
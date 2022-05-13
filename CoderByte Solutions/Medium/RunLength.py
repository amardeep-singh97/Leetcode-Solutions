"""
Question:-

Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. 
This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. 
For example: "wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.
Examples
Input: "aabbcde"
Output: 2a2b1c1d1e 

"""

def RunLength(strParam):
  res = ""
  first = strParam[0]
  counter = 0
  for i in range(len(strParam)):
    if strParam[i]==first:
      counter+=1
    else:
      res += str(counter)+first
      first = strParam[i]
      counter = 1
  res += str(counter)+first
  return res
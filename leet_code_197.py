#https://leetcode.com/problems/maximum-number-of-words-you-can-type/
#Maximum Number of Words You Can Type
#There is a malfunctioning keyboard where some letter keys do not work. 
#All other keys on the keyboard work properly.
#Given a string text of words separated by a single space (no leading or trailing spaces) 
#and a string brokenLetters of all distinct letter keys that are broken, return the number of 
#words in text you can fully type using this keyboard.
#Example 1:
#Input: text = "hello world", brokenLetters = "ad"
#Output: 1
#Explanation: We cannot type "world" because the 'd' key is broken.
#Example 2:
#Input: text = "leet code", brokenLetters = "lt"
#Output: 1
#Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
#Example 3:
#Input: text = "leet code", brokenLetters = "e"
#Output: 0
#Explanation: We cannot type either word because the 'e' key is broken.

[text.strip().split()[i] for i in range(len(text.strip().split())) 
          if len(set(text.strip().split()[i]).intersection(brokenLetters))==0]
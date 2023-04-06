#https://leetcode.com/problems/second-largest-digit-in-a-string/
#Second Largest Digit in a String
#Given an alphanumeric string s, return the second largest numerical 
#digit that appears in s, or -1 if it does not exist.
#An alphanumeric string is a string consisting of lowercase English letters and digits.
#Input: s = "dfa12321afd"
#Output: 2
#Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
#Input: s = "abc1111"
#Output: -1
#Explanation: The digits that appear in s are [1]. There is no second largest digit.

int(list(set(sorted([i for i in s if i.isdigit()])))[1])
#https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
#Replace All ?'s to Avoid Consecutive Repeating Characters
#Given a string s containing only lowercase English letters and the '?' character, convert all 
#the '?' characters into lowercase letters such that the final string does not contain 
#any consecutive repeating characters. You cannot modify the non '?' characters.
#It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
#Return the final string after all the conversions (possibly zero) have been made. 
#If there is more than one solution, return any of them. It can be shown that an answer 
#is always possible with the given constraints.
#Example 1:
#Input: s = "?zs"
#Output: "azs"
#Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. 
#Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
#Example 2:
#Input: s = "ubv?w"
#Output: "ubvaw"
#Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications 
#as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".

[s.replace("?", [chr(i+97) for i in range(26)][j]) for i in range(len(s)) for j in 
              range(len([chr(i+97) for i in range(26)])) if [chr(i+97) for i in range(26)][j]!="z"]
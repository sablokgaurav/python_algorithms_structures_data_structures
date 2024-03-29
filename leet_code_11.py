#Letter Case Permutation (Medium)
#Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
#Return a list of all possible strings we could create. Return the output in any order.
#Example 1:
#Input: s = "a1b2"
#Output: ["a1b2","a1B2","A1b2","A1B2"]
#Example 2:
#Input: s = "3z4"
#Output: ["3z4","3Z4"]
from more_itertools import substrings
print([i for i in (''.join(i) for i in (list(substrings(list(s.upper() + s.lower()))))) if len(i) >= 4])
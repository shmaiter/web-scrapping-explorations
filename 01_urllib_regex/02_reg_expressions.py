import re

"""
re.IGNORECASE = case insensitive  
* = zero or more instances of the same instance
. = a single character, can be any, is a must and cannot be more than one.
? = non-greedy, it matches the shortest possible string of text
"""

print(re.findall("ab*c", "ac")) # ['ac']
print(re.findall("ab*c", "abdc")) # []
print(re.findall("ab*c", "abcABC", re.IGNORECASE)) # ['abc', 'ABC']
print(re.findall("a.c", "abc")) # ['abc']
print(re.findall("a.c", "abbc")) # []
print(re.findall("a.c", "ac")) # []


match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group()) # 'ABC'

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string) # greedy
print(string) # 'Everything is ELEPHANTS.'

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string) # NOT greedy
print(string) # 'Everything is ELEPHANTS if it's in ELEPHANTS.'




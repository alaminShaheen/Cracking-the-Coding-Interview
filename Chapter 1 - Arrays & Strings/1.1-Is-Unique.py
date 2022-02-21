# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures? 

# using hashmap
def isUnique1(s: str) -> bool:
    hasOccurrence = {}
    for char in s:
        if char in hasOccurrence:
            return False
        else:
            hasOccurrence[char] = True
    return True

# using set
def isUnique2(s: str) -> bool:
    hasOccurrence = set()
    for char in s:
        if char in hasOccurrence:
            return False
        else:
            hasOccurrence.add(char)
    return True

# using bitset
def isUnique3(s: str) -> bool:
    bitset = 0
    for char in s:
        mask = 1 << char - ord('a') 
        if bitset & mask:
            return False
        else:
            bitset &= mask
    return True

# using sort
def isUnique4(s: str) -> bool:
    s.sort()
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True

# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other. 

# using hashmap
def checkPermutation1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in t:
        if char not in t:
             return False
        else:
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]
    return len(freq) == 0


# using sort
def checkPermutation2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s = "".join(sorted(s))
    t = "".join(sorted(t))

    for i in range(len(t)):
        if t[i] != s[i]:
            return False
    return True

        
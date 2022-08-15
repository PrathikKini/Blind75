#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Input: s = "anagram", t = "nagaram"
#Output: true

def Anagram(s,t):
    if len(s)!=len(t):
        return False
    CountS, CountT = {}, {}

    for i in range(len(s)):
        CountS[s[i]] = 1 + CountS.get(s[i],0)
        CountT[t[i]] = 1 + CountT.get(t[i],0)
    
    for c in CountS:
        if CountS[c] != CountT.get(c,0):
            return False
    return True

print(Anagram("anagram","nagaram"))

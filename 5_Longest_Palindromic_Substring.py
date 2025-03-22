# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

def longestPalSub(s):
    resInd = resLen = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > resLen:
                resInd = l
                resLen = r-l+1
            l -= 1
            r += 1

        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > resLen:
                resInd = l
                resLen = r-l+1
            l -= 1
            r += 1
    return s[resInd:resInd+resLen]

print(longestPalSub(s = "babad"))
print(longestPalSub(s = "cbbd"))
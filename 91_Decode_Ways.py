# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'
# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").
# Example 1:
# Input: s = "12"
# Output: 2
# Explanation:
# "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation:
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "06"
# Output: 0
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

def decodeWays(s):
    dp = dp2 = 0
    dp1 = 1

    for i in range(len(s)-1,-1,-1):
        if s[i] == "0":
            dp = 0
        else:
            dp = dp1

        if i+1 < len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
            dp += dp2
        
        dp, dp1, dp2 = 0, dp, dp1
    return dp1

print(decodeWays("12"))
print(decodeWays("226"))
print(decodeWays("06"))
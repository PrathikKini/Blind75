"""
Input: s = "()"  Output: true
Input: s = "()[]{}" Output: true
Input: s = "(]" Output: false
"""
def parenthesis(s):
    stack = []
    closetoOpen = {"}":"{","]":"[",")":"("}

    for c in s:
        if c in closetoOpen:
            if stack and stack[-1] == closetoOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

print(parenthesis("()[]{}"))
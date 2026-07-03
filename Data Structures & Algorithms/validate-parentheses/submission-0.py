class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        c={")":"(","]":"[","}":"{" }
        for ss in s:
            if ss in c:
                if stack and stack[-1]== c[ss]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ss)
        return True if not stack else False
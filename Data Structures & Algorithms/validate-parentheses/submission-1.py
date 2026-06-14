class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                if pairs[i]!=stack[-1]:
                    return False
                stack.pop()
        return not stack




        
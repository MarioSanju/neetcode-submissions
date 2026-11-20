class Solution:
    def isValid(self, s: str) -> bool:


        stack = []
        pairs = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for char in s:
            if char in "([{":
                stack.append(char)
                
            else:
                if not stack:
                    return False
                aux = stack.pop()
                if  aux != pairs[char]:
                    return False
                  
        return not stack






































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




        
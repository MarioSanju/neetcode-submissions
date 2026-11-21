class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for op in tokens:
            if op == "+":
                plus = stack.pop()
                plus += stack.pop()
                stack.append(plus)

            elif op == "*":
                product = stack.pop()
                product *= stack.pop()
                stack.append(product)
            
            elif op == "/":
                plus = stack.pop()
                plus = int(stack.pop()/plus)
                stack.append(plus)
            
            elif op == "-":
                res = stack.pop()
                res = stack.pop() - res
                stack.append(res)
            
            else:
                stack.append(int(op))
            
        return stack[-1]
            

            

        
        
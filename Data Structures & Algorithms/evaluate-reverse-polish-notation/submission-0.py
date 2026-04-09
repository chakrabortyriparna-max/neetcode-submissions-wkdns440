class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                b, a = stack.pop(), stack.pop()
                # Use float division then cast to int to truncate toward zero
                stack.append(int(a / b))
            else:
                # Token is a number
                stack.append(int(t))
                
        return stack[0]
        
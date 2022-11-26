# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for character in tokens:
            if character == "+":
                stack.append(stack.pop() + stack.pop())
            elif character == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif character == "*":
                stack.append(stack.pop() * stack.pop())
            elif character == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(character))
                
        return stack[0]
                

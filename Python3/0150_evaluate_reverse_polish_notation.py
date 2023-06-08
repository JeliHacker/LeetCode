# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        operations = {"+", "-", "*", "/"}

        for item in tokens:
            if item in operations:
                num2 = int(my_stack.pop())
                num1 = int(my_stack.pop())
                print(num1, num2)
                if item == "+":
                    my_stack.append(num1 + num2)
                elif item == "-":
                    my_stack.append(num1 - num2)
                elif item == "*":
                    my_stack.append(num1 * num2)
                elif item == "/":
                    my_stack.append(int(num1 / num2))
            
            else:
                my_stack.append(item)

        return int(my_stack[0])
              

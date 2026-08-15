class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Logic:
        # Stack implementation
        # 1. Iterate through array
        # 2. If integer, push to stack
        # 3. If operand, pop two elements from stack, calculate value, push calculated value to stack

        stack = []
        operands = ['+', '-', '*', '/']

        for val in tokens:        
            if val not in operands:
                stack.append(val)
            else:
                operator2 = int(stack.pop())
                operator1 = int(stack.pop())
                if val == "+":
                    res = operator1 + operator2
                    stack.append(res)
                elif val == "-":
                    res = operator1 - operator2
                    stack.append(res)
                elif val == "*":
                    res = operator1 * operator2
                    stack.append(res)
                elif val == "/":
                    res = operator1 / operator2
                    stack.append(res)


        return int(stack[0])
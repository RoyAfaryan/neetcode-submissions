class Solution:
    def isValid(self, s: str) -> bool:
        
        # Logic:
        # Stack implementation
        # 1. Push open symbols to the top of the stack
        # 2. If closed symbol, compare to the top of the stack: eg. does '[' = ']'
        # 3. If comparison fails, return false
        # 4. If all comparisons are fine, return true

        symbols = {')':'(', '}':'{', ']':'['}
        op = ['(', '{', '[']
        cl = [')', '}', ']']
        stack = []

        for c in s:
            if c in op:
                stack.append(c)
            elif c in cl:
                if stack != []:
                    if symbols.get(c) == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        
        return True if stack == [] else False
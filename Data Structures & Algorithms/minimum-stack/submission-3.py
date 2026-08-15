class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if self.minVal == None:
            self.minVal = val
            self.minStack.append((val, self.minVal))
        elif self.minVal < val:
            self.minStack.append((val, self.minVal))
        else:
            self.minVal = val
            self.minStack.append((val, self.minVal))

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if not self.minStack:
            self.minVal = None
        else:
            self.minVal = self.minStack[-1][1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][1]

        

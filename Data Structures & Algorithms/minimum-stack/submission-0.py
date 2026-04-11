class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.myStack = []

    def push(self, val: int) -> None:
        if not self.myStack:
            self.myStack.append(0)
            self.min = val
        else:
            self.myStack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.myStack:
            return
        popElement = self.myStack.pop()
        if popElement < 0:
            self.min = self.min - popElement

    def top(self) -> int:
        top = self.myStack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min      

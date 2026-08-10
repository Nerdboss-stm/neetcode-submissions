class MinStack:

    def __init__(self):
        self.data = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minstack or val <= int(self.minstack[-1]):
            self.minstack.append(val)
        

    def pop(self) -> None:
        if self.data:
            # If the removed value is the minimum, remove it from min_stack too
            if self.data[-1] == self.minstack[-1]:
                self.minstack.pop()
            self.data.pop()
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        

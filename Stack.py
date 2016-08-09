class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, elt):
        """Insert an element in the stack"""
        if len(self.stack) == 0:
            self.stack = [elt]
            return True
        elif self.canInsert(elt):
            self.stack.insert(0,elt)
            return True
        else:
            TTT.TTTException(3)
        return False

    def pop(self):
        """Erase the element in the top of the stack"""
        self.stack.pop(0)

    def canInsert(self, elt):
        """Verify if a value can be inserted in the stack"""
        if elt in self.stack:
            return False
        return True

    def getStack(self):
        """Return the entire stack content"""
        return self.stack

    def top(self):
        """Return the value on top of the stack"""
        return self.stack[0]

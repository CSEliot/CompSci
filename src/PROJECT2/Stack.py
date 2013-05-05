class Stack: 
    
    def __init__(self): 
        self.theStack = [] 

    def top(self): 
        # calls another of stack's functions that'll return true/false 
        if self.isEmpty():
            # worth noting that IF statements read strings as True.
            # This is a false positive, bad code design. Because if top is 
            # called, and it can't return anything, it'll return a string,
            # which when used with a try/catch or IF, will throw a false positiv
            return "Empty Stack" 
        else:
            # will return top if not empty, but not remove it. 
            return self.theStack[-1] 

    def isEmpty(self): 
        return len(self.theStack) == 0 # no need to explain this

    def push(self, item): 
        # though this works, this isn't literal enough to represent a stack.
        # again, bad code design. It SHOULD literally add to the end of the list
        self.theStack.append(item)  
    
    def pop(self): 
        if not self.isEmpty():
            # lists HAVE a pop() function. I mean, really? Yes, this is more
            # literal, but a student should know what POP does, or they can 
            # google it, which takes all of 30 seconds. i know, i counted. 
            temp = self.theStack[- 1] 
            del(self.theStack[- 1]) 
            return temp 
        else: 
            return "Empty Stack"
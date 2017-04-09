class linkedList:
    
    
    def __init__(self, l=[]):

        if(type(l) == list):
            self.val = l[0]
            if(not l[1:]):
                self.next = None
                self.tail = self
            else:
                self.next = linkedList(l[1:])
                self.tail = self.next
        else:
            self.val = l
            self.next = None
            self.tail = self 
            
            
    def __getitem__(self, key):
        
        if(key < 0):
            raise IndexError("Index Out Of range")
        
        elif(key == 0):
            return self.val
        return self.next[key - 1]
    
    def __setitem__(self, key, val):
    
        if(key < 0):
            raise IndexError("Index Out Of range")
        
        elif(key == 0):
            self.val = val
        
        else:
            self.next[key - 1] = val

    
    def __add__(self, y):
        
        if(self.next):
            self.next + y
        else:
            self.next = linkedList(y)
        

    def __add__(self, y):
        
        if(self.next):
            self.next + y
        else:
            self.next = linkedList(y)
   
    def __radd__(self, y):
        
        return y + self.list()

    def __mul__(self, y):
        
        if(y == 0):
            return None
        else:
            return self + self * (y - 1)
        
    def __rmul__(self, y):
        
        return self * y
        
    def __contains__(self, x):
        
        if(self.next):   
            return (self.val == x) or (x in self.next)
        return (self.val == x)
        
    def __len__(self):
        
        if(self.next):
            return 1 + len(self.next)
        else:
            return 1
        
    def list(self):
        
        if(self.next):
            return [self.val] + self.next.list()
        
        return [self.val]
 
    def __iter__(self):
        
        return linkediter(self)
    
    def append(self, val):
        
        if(self.next):
            self.next.append(val)
            return None
        else:
            self.next = linkedList(val)
            return self.next
        
    def __str__(self):
        
        if(self.next):
            return str(self.val) + "->" + str(self.next)
        return str(self.val)
    
class linkediter:
    
    def __init__(self, l):
        
        self.list = l 
        
    def __next__(self):
        
        if(self.list == None):
            raise StopIteration     
        
        c = self.list[0]
        self.list = self.list.next
        print(self.list)
        return c


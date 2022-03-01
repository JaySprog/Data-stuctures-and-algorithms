class node:
    def __init__(self,x):
        self.val=x
        self.nf=None

class linkedlist:
    def __init__(self):
        self.whole=None

    def add(self,x):
        node_struct=node(x)

        if self.whole == None:
            self.whole=node_struct
            return
        
        temp=self.whole
        while temp.nf!=None:
            temp=temp.nf
        temp.nf=node_struct

    def printvalue(self):
        temp=self.whole
        while temp is not None:
            print(temp.val)
            temp=temp.nf

    def get_nth(self,n):
        if n<0:
            print('negative indexing not accepted')
            return
        
        if self.whole is None:
            print('empty list')
            return
        
        temp=self.whole
        for i in range(0,n+1):
            if temp==None:
                print('index exceeded')
                return
            by=temp
            temp=temp.nf
        print('index:',n,'element is:',by.val)    
        
a=linkedlist()
a.add(7)
a.add(2)
a.add(3)
a.add(1)
a.add(7)
a.add(25)
a.printvalue()
a.get_nth(6)


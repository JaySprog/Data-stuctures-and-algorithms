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


    def delete(self,position):
        if self.whole is None:
            return
        
        if position==0:
            self.whole=self.whole.nf
            return
        
        temp=self.whole
        for i in range(0,position):
            by=temp
            temp=temp.nf
        by.nf=temp.nf

a=linkedlist()
a.add(8)
a.add(2)
a.add(3)
a.add(1)
a.add(7)
a.printvalue()
a.delete(0)
a.printvalue()

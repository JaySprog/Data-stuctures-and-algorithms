class node:
    def __init__(self,x):
        self.val=x
        self.nf=None

class linkedlist:
    def __init__(self):
        self.whole=None

    def prepend(self,x):
        node_struct=node(x)
        node_struct.nf=self.whole
        self.whole=node_struct

    def deleteval(self,x):
        if self.whole.val==x:
            self.whole=self.whole.nf
            return 

        temp=self.whole
        while temp.nf is not None:
            if temp.nf.val==x:
                temp.nf=temp.nf.nf
            temp=temp.nf

            if temp==None:
                return

            

    def printvalue(self):
        temp=self.whole
        while(temp):
            print(temp.val)
            temp=temp.nf
       
                
a=linkedlist()
a.prepend(5)
a.prepend(7)
a.prepend(9)
a.prepend(9)
a.prepend(4)
a.prepend(3)
a.deleteval(3)
a.printvalue()

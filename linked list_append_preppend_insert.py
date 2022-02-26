
class node:
    def __init__(self,x):
        self.val=x
        self.nf=None

class linkedlist:
    def __init__(self):
        self.whole=None

    def addfront(self,x):
        node_structure=node(x)

        if self.whole is None:
            self.whole=node_structure
            return

        if self.whole is not None:
            temp=self.whole
            while(temp.nf):
                temp=temp.nf
            temp.nf=node_structure
            
            
    def addback(self,x):
        node_structure=node(x)

        node_structure.nf=self.whole

        self.whole=node_structure

    def insertafter(self, prev_node, x):
        node_structure=node(x)
        
        node_structure.nf=prev_node.nf

        prev_node.nf=node_structure

        

    def printvalue(self):
        temp=self.whole
        while(temp):
            print(temp.val)
            temp=temp.nf

             

a=linkedlist()
a.addfront(5)
a.addfront(7)
a.addfront(9)
a.addback(4)
a.insertafter(a.whole,11)
a.addback(2)
a.printvalue()


           
            

        

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

    def remove_duplicates(self):
        a=[]
        temp=self.whole
        while(temp.nf):
            a.append(temp.val)
            if temp.nf.val in a:
                temp.nf=temp.nf.nf
                continue
            temp=temp.nf

    def printvalue(self):
        temp=self.whole
        while(temp):
            print(temp.val)
            temp=temp.nf
            
                  
a=linkedlist()
a.add(10)
a.add(12)
a.add(11)
a.add(11)
a.add(12)
a.add(11)
a.add(10)
a.add(12)
a.add(25)
a.add(15)
a.add(10)

a.remove_duplicates()
a.printvalue()






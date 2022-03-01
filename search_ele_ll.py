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

    def search(self,ele):
        temp=self.whole
        while temp is not None:
            if temp.val==ele:
                print('ele',ele,'is present')
                return
            temp=temp.nf
        print('ele',ele, 'is not present')    
        


a=linkedlist()
a.add(7)
a.add(2)
a.add(3)
a.add(1)
a.add(7)
a.printvalue()
a.search(12)


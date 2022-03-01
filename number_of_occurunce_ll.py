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
        if self.whole is None:
            print('empty list')
            return
        
        count=0
        temp=self.whole
        while temp is not None:
            if temp.val==ele:
                count=count+1
            temp=temp.nf
            
        if count==0:
            print('element',ele, 'is not present')

        else:
            print('occurunces of element',ele,':',count,'times')   
        


a=linkedlist()
a.add(7)
a.add(2)
a.add(3)
a.add(1)
a.add(7)
a.add(7)
a.add(3)
a.printvalue()
a.search(7)

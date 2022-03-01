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


    def get_middle(self):
        if self.whole is None:
            print('empty list')
            return

        if self.whole.nf is None:
            print('only value is:',self.whole.val)
            return


        temp=self.whole
        count=0
        while temp is not None:
            temp=temp.nf
            count=count+1

        l=count
        n=l//2

        temp=self.whole
        for i in range(0,n+1):
            by=temp
            temp=temp.nf
        print('middle element is:', by.val)    
        

a=linkedlist()
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.printvalue()
a.get_middle()


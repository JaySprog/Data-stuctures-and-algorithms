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

    def create_loop(self):
        self.whole.nf.nf.nf.nf=self.whole.nf.nf
        
    def detect_loop(self):
        temp=self.whole
        a=[]
        while temp is not None:
            if id(temp.val) in a:
                print('loop found')
                print(temp.val,id(temp.val))
                return
            print(temp.val,id(temp.val))
            a.append(id(temp.val))
            temp=temp.nf

        print('no loop found')
            

a=linkedlist()
a.add(2)
a.add(3)
a.add(5)
a.add(9)
a.create_loop()
a.detect_loop()



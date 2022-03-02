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
        self.whole.nf.nf.nf.nf=self.whole.nf
        
    def detect_loop_floyd(self):
        tortoise=self.whole
        rabbit=self.whole
        while (rabbit!=None and rabbit.nf!=None):
            rabbit=rabbit.nf.nf
            tortoise=tortoise.nf
            if rabbit==tortoise:
                print('loop found')
                return
        print('loop not found')


a=linkedlist()
a.add(2)
a.add(3)
a.add(5)
a.add(9)
a.create_loop()
a.detect_loop_floyd()

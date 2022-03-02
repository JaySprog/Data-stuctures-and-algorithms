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

    def palindrome_check(self):
        a=[]
        temp=self.whole
        while(temp):
            a.append(temp.val)
            temp=temp.nf

        print(a)    
        
        temp=self.whole    
        while(temp):
            if temp.val!=a.pop():
                print('list is not palindrome')
                return
            temp=temp.nf    

        print('list is palindrome')   

a=linkedlist()
a.add('j')
a.add('a')
a.add('h')
a.add('a')
a.add('j')

a.palindrome_check()



            

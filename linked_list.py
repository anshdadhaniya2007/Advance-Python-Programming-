class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head , self.tail=None,None
    def push_front(self,val):
        newnode=node(val)
        if self.head==None:
            self.head=self.tail=newnode
            return
        newnode.next=self.head
        self.head=newnode
    def show(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def pop_front(self):
        if self.head==None:
            print("linked list is empty!!!")
            return
        print(self.head.data ," has been removed")
        self.head=self.head.next
        if self.head==None:
            self.tail=None
i=True
a=linked_list()
while True:
    b=int(input("enter the number for choise \n 1. Add node at front\n 2. Remove a node from front \n 3. See linked list\n 4. Exit\n"))
    if(b==1):
        val=int(input("enter the number to add"))
        a.push_front(val)
        a.show()
    elif(b==2):
        a.pop_front()
        a.show()
    elif(b==3):
        a.show()
    elif(b==4):
        break
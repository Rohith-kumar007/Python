class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.head.next = self.head  
        else:
            self.temp = self.head
            while self.temp.next != self.head:
                self.temp = self.temp.next
            self.temp.next = newnode
            newnode.next = self.head  

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        self.temp = self.head
        while True:
            print(self.temp.data, end=' ')
            self.temp = self.temp.next
            if self.temp == self.head:
                break
        print()

    def delete_at_front(self):
        self.head=self.head.next
        self.tail.next=self.head
        
    def delete_at_end(self):
        self.temp=self.head
        while self.temp.next.next!=self.head:
            self.temp=self.temp.next
        self.temp.next.next=None
        self.temp.next=self.head
        self.tail=self.temp
        
    def delete_at_mid(self,pos):
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i+=1
        temp=self.temp.next.next
        self.temp.next.next=None
        self.temp.next=temp

obj = CircularSLL()
while(1):
    print("1.create 2.display 3.exit 4.delete_at_front 5.delete_at_mid 6.delete_at_end")
    choice = int(input("enter the choice: "))
    if choice == 1:
        data = int(input("enter the data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        break
    elif choice == 4:
        obj.delete_at_front()
    elif choice == 5:
        pos = int(input("enter position: "))
        obj.delete_at_mid(pos)
    elif choice == 6:
        obj.delete_at_end()
    else:
        print("invalid choice")













        

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class CircularSLL:
    def _init_(self):
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

    def insert_at_front(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.head.next = self.head
        else:
            self.temp = self.head
            while self.temp.next != self.head:
                self.temp = self.temp.next
            newnode.next = self.head
            self.temp.next = newnode
            self.head = newnode

    def insert_at_mid(self, data, pos):
        if pos == 1:
            self.insert_at_front(data)
            return
        newnode = Node(data)
        self.temp = self.head
        i = 1
        while i < pos - 1 and self.temp.next != self.head:
            self.temp = self.temp.next
            i += 1
        if self.temp.next == self.head and i < pos - 1:
            print("Position out of bounds.")
            return
        newnode.next = self.temp.next
        self.temp.next = newnode

    def insert_at_end(self, data):
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

obj = CircularSLL()
while(1):
    print("1.create 2.display 3.exit 4.insert_front 5.insert_mid 6.insert_end")
    choice = int(input("enter the choice: "))
    if choice == 1:
        data = int(input("enter the data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        break
    elif choice == 4:
        data = int(input("enter the data: "))
        obj.insert_at_front(data)
    elif choice == 5:
        data = int(input("enter the data: "))
        pos = int(input("enter position: "))
        obj.insert_at_mid(data, pos)
    elif choice == 6:
        data = int(input("enter the data: "))
        obj.insert_at_end(data)
    else:
        print("invalid choice")


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            self.temp = newnode
        else:
            self.temp.next = newnode
            self.temp = newnode

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data, end=' ')
            self.temp = self.temp.next
        print()

    def delete_from_front(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.temp = self.head
            while self.temp.next.next is not None:
                self.temp = self.temp.next
            self.temp.next = None

    def delete_from_mid(self, pos):
        if self.head is None:
            print("List is empty")
        elif pos == 1:
            self.delete_from_front()
        else:
            self.temp = self.head
            i = 1
            while i < pos - 1:
                self.temp = self.temp.next
                i += 1
            if self.temp.next is not None:
                self.temp.next = self.temp.next.next
            else:
                print("Position out of range")

obj = SLL()
while True:
    print("1.create 2.display 3.exit 4.delete_front 5.delete_mid 6.delete_end")
    choice = int(input("enter the choice: "))
    if choice == 1:
        data = int(input("enter the data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        break
    elif choice == 4:
        obj.delete_from_front()
    elif choice == 5:
        pos = int(input("enter position: "))
        obj.delete_from_mid(pos)
    elif choice == 6:
        obj.delete_from_end()
    else:
        print("invalid choice")

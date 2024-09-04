class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.temp=None

    def create(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode

    def display(self):
        self.temp=self.head
        while self.temp!=None:
            print(self.temp.data, end=' ')
            self.temp=self.temp.next
        print()


    def Search(self,search):
        result=0
        self.temp=self.head
        while self.temp!=None:
            if self.temp.data==search:
                result=1
            self.temp=self.temp.next
        if result:
            print("found")
        else:
            print("not found")

    def insert_at_front(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode

    def insert_at_middle(self,data,pos):
        newnode=node(data)
        i=1
        self.temp=self.head
        while i < pos-1:
            self.temp=self.temp.next
            i+=1
        print(i)
        newnode.next=self.temp.next
        self.temp.next=newnode

      def count(self, search):
        count = 0
        self.temp = self.head
        while self.temp is not None:
            if self.temp.data == search:
                count += 1
            self.temp = self.temp.next
        print(f"The element {search} occurs {count} time(s) in the list.")  

        
    def insert_at_end(self,data):
        newnode=node(data)
        self.temp=self.head
        while self.temp.next != None:
            self.temp=self.temp.next
        self.temp.next=newnode
        
obj=SLL()
while 1:
    print("1.create 2.display 3.exit 4.insert_at_front 5.insert_at_end 6.insert_at_middle 7.search:")
    choice=int(input("Enter a choice :"))
    if(choice==1):
        data=int(input("Enter data :"))
        obj.create(data)
    elif(choice==2):
        obj.display()
    elif(choice==3):
        break
    elif(choice==4):
        data=int(input("Enter a data :"))
        obj.insert_at_front(data)
    elif(choice==5):
        data=int(input("Enter a data :"))
        obj.insert_at_end(data)
    elif(choice==6):
        data=int(input("Enter a data : "))
        pos=int(input("Enter a position : "))
        obj.insert_at_middle(data,pos)
    elif choice==7:
        search=int(input("enter the search"))
        obj.Search(search)

    elif choice==8:
        search=int(input("Enter a search :"))
        obj.

    else :
        print("Invalid operation")
        

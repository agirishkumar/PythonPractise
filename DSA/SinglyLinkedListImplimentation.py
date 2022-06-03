#defining a node
class Node:
    #constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# A linkedlist class with head node
class LinkedList:
    def __init__(self):
        self.head = None

    #insertion method for Linkedlist
    def insert(self,data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    # print method for LinkedList
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert('Asuran')
LL.insert('Hi')
LL.insert(10)
LL.printLL()

 
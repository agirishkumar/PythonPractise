#defining Node


class Node:
    # constructor
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

#creating linkedlist

class LinkedList:
    def __init__(self):
        self.head = None
    

    #inserting data
    def insert(self,data):
        newNode = Node(data)
        
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printNodes(self):
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
LL.printNodes()
from ll import LinkedList
from ll import Node
class Queue:
    def __init__(self,llist):
        self.llist=llist
        self.front=None
        self.rear=None
    
    def enqueue(self,key):
        if not self.front:
            self.front=Node(key)
        self.rear=Node(key)
        self.llist.append(key)
    
    def dequeue(self):
        self.llist.delete_node_at_pos(0)
        self.front=self.llist.head

    def get_front(self):
        if self.front:
            return self.front.data
    
    def get_rear(self):
        if self.rear:

            return self.rear.data

llist=LinkedList()
Q=Queue(llist)
Q.enqueue(1)
Q.enqueue(2)
print(Q.get_front())
print(Q.get_rear())
Q.dequeue()
print(Q.get_front())
print(Q.get_rear())
    






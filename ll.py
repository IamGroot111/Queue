class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return

        cur_node=self.head
        while cur_node.next:
            cur_node=cur_node.next

        cur_node.next=Node(data)

    def prepend(self,data):
        
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_at_pos(self,data,pos):

        if pos==0:
            self.prepend(data)
            return
        
        count=0
        prev=None
        cur_node=self.head
        while(cur_node and count!=pos):
            prev=cur_node
            cur_node=cur_node.next
            count+=1
        
        if not cur_node:
            if(pos==count):
                self.append(data)
            return

        new_node=Node(data)
        prev.next=new_node
        new_node.next=cur_node
        

    def delete_node(self,data):

        cur_node=self.head

        if (cur_node and cur_node.data==data):
            self.head=cur_node.next
            cur_node==None
            return

        prev_node=None

        while(cur_node and cur_node.data!=data):
            prev_node=cur_node
            cur_node=cur_node.next
        
        if cur_node==None:
            return
        
        prev_node.next=cur_node.next
        cur_node=None
    
    def delete_node_at_pos(self,pos):
        
        cur_node=self.head
        
        if(pos==0):
            self.head=cur_node.next
            cur_node=None
            return
            
        count=0
      
        prev_node=None

        while(count!=pos and cur_node):
            prev_node=cur_node
            cur_node=cur_node.next
            count+=1

        if not cur_node:
            return

        prev_node.next=cur_node.next
        cur_node=None    





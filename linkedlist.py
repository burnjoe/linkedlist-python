class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, node: Node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def display(self):
        cur = self.head
        while cur != None:
            print(cur.val, end=" -> ")
            cur = cur.next
        print(cur)

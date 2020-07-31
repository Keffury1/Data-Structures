"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev



class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value


    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    def move_to_front(self, node):
        if node is not self.tail:
            self.delete(node)
            self.add_node_to_tail(node)
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)
    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.remove()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.remove()
        else:
            node.remove() 
    def get_max(self):
        if not self.head:
            return None
        
        max_value = self.head.value
        curr = self.head
        while curr:
            if curr.value > max_value:
                max_value = curr
            curr = curr.next
            return max_value

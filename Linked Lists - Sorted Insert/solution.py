""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head is None or data < head.data:
        result = Node(data)
        result.next = head
        return result

    current = head
    while current.data is not None:
        if data > current.data and (current.next is None or data < current.next.data):
            
            new = Node(data)
            next = current.next
            current.next = new
            new.next = next
            return head
        current = current.next

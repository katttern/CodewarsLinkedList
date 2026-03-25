class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    first_head = Node(head.data)
    second_head = Node(head.next.data)

    first_tail = first_head
    second_tail = second_head
    current = head.next.next
    add_to_first = True

    while current is not None:
        new_node = Node(current.data)
        if add_to_first:
            first_tail.next = new_node
            first_tail = new_node
        else:
            second_tail.next = new_node
            second_tail = new_node
        if add_to_first == True:
            add_to_first = False
        else:
            add_to_first = True
        current = current.next

    return Context(first_head, second_head)

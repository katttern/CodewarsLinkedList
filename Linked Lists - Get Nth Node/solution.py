from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    current = node
    cur_index = 0
    while current.data is not None:
        if cur_index == index:
            return current
        cur_index += 1
        current = current.next

from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None
    nodes_data_list = list_repr.split(' -> ')
    nodes_data_list.remove('None')
    node = Node(int(nodes_data_list[0]))
    current = node
    for index, element in enumerate(nodes_data_list):
        try:
            current.next = Node(int(nodes_data_list[index+1]))
            current = current.next
        except IndexError:
            return node

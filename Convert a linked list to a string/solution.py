def stringify(node):
    result = ''
    while node is not None:
        result += f'{node.data} -> '
        node = node.next
    result += 'None'
    return result
  

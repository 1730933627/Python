class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None # 
        
print('定义 Node 完成')
node1 = Node(1) 
node2 = Node(2) 
node3 = Node(3)
node1.pointer = node2
node2.pointer = node3
def print_list(node):
    if node.pointer:
        print(node.value, end='->')
    else:
        print(node.value,)
    if (node.pointer):
        print_list(node.pointer) # 什么是递归
print_list(node1)

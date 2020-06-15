class Stack:
    def __init__(self):
        self.items = []

	# 栈是否为空
    def is_empty(self):
        return self.items == []

    # 向栈中添加一个元素
    def push(self, item):
        self.items.append(item)
        
    # 栈中弹出一个元素
    def pop(self):
        return self.items.pop()

    # 获取栈顶元素（不弹出）
    def peek(self):
        if len(self.items):
            return self.items[len(self.items)-1]
        return None

    # 查看栈中元素个数
    def size(self):
        return len(self.items)
    

# 打印栈
def print_stack(stack):
    print('{:↑^11}'.format(' 栈顶 '))
    for i in range(len(stack.items)):
        print('{:^11}'.format(stack.items[len(stack.items) - i - 1]))
    print('{:↑^11}'.format(' 栈底 '))
    
print('定义 Stack 成功')

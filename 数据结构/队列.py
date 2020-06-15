class Queue:
    def __init__(self):
        self.items = []
         
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
        
# 定义一个方法来打印一个队列
def print_queue(queue):
    print('{:↑^11}'.format(' 队头 '))
    for i in range(len(queue.items)):
        print('{:^11}'.format(queue.items[len(queue.items) - i - 1]))
    print('{:↑^11}'.format(' 队尾 '))
    
# 点击左上角，或按 Ctrl+Enter 来运行这段代码
print('定义 Queue 成功')

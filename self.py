class Self():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print('init被调用！')
    def prei(self):
        return (self.x+self.y)*2
    def area(self):
        return self.x * self.y
    def __del__(self):
        print('del被调用')

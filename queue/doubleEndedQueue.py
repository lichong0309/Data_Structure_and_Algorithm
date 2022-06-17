'''
Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小

'''

class doubleEndedQueue(object):
    def __init__(self) -> None:
        self.item = []   # 初始化为空的双端队列
        
    # is_empty() 判断双端队列是否为空
    def is_empyt(self):
        if self.item == []:
            print("双端队列为空")
            return False
        if self.item != []:
            print("双端队列不为空")
            return True
        
        
    # size() 返回队列的大小
    def size(self):
        return len(self.item)
    
    # add_front(item) 从队头加入一个item元素
    def add_front(self, item):
        self.item.insert(0, item)
        
    # add_rear(item) 从队尾加入一个item元素
    def add_rear(self, item):
        self.item.insert(len(self.item), item)
    
    # remove_front() 从队头删除一个item元素
    def remove_front(self):
        self.item.pop(0)
        
    # remove_rear() 从队尾删除一个item元素
    def remove_rear(self):
        self.item.pop(len(self.item)-1)
        
    # 打印双端队列
    def itemItor(self):
        print(self.item)
        
        
if __name__ == "__main__":
    d = doubleEndedQueue()
    d.is_empyt()
    d.add_front("hello")
    d.add_front("world")
    d.add_front("itcast")
    d.itemItor()
    
    d.add_rear("new")
    d.add_rear("year")
    d.itemItor()
    
    d.remove_front()
    d.remove_rear()
    d.itemItor()
    
    
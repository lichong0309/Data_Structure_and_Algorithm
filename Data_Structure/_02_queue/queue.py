'''
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
'''

class queue(object):
    def __init__(self) -> None:
        self.item = []          # 初始化为空的队列
        
    # is_empty() 判断一个队列是否为空
    def is_empyt(self):
        if self.item == []:
            print("队列为空")
            return False
        else:
            print("队列不为空")
            return True


    # enqueue(item) 往队列中添加一个item元素，在队列末尾添加
    def enqueue(self, item):
        return self.item.insert(len(self.item), item)
    
    # dequeue() 从队列头部删除一个元素
    def dequeue(self):
        self.item.pop(0)
        return True
    
    # 打印队列
    def itemItor(self):
        print(self.item)
    
    # size() 返回队列的大小
    def size(self):
        return len(self.item)
    

if __name__ == "__main__":
    q = queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    q.itemItor()
    
    q.dequeue()
    q.itemItor()
    
    print(q.size())
'''
is_empty() 链表是否为空
length() 链表长度
items() 获取链表数据迭代器
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
find(item) 查找节点是否存在
'''


from locale import currency
from tkinter import N


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None 

class circleSingleLink(object):
    def __init__(self) -> None:
        self.head = None 
        
    def is_empty(self):
        if self.head == None:
            print("链表为空")
            return False
        else:
            print("链表不为空")
            return True
        
        
    # length() 链表长度
    def length(self):
        if self.head == None:
            print("链表为空")
        else:
            count = 0
            cur = self.head 
            while cur.next != self.head:
                count += 1
                cur = cur.next
            # cur目前指向最后一个节点
            count += 1
            print("链表的长度为：",count)
        
    # items() 获取链表数据迭代器
    def items(self):
        if self.head == None:
            print("链表为空")
        else:
            self.length()
            cur = self.head 
            itemList = []
            while cur.next != self.head:
                itemList.append(cur.data)
                cur = cur.next
            # cur指针目前指向最后一个节点
            itemList.append(cur.data)
            print("链表的数据迭代器为：", itemList)
            
    
    # add(item) 链表头部添加元素
    def addInHead(self, item):
        n = Node(item)
        # 1.判断是否为空
        if self.head == None:
            self.head = n
            self.head.next = self.head
        # 链表不为空
        else:
            # 添加节点，next指向head
            n.next = self.head  
            # 遍历到最后一个节点
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            # cur节点现在指向最后一个节点
            cur.next = n
            self.head = n
    
    
    # append(item) 链表尾部添加元素
    def append(self, item):
        n = Node(item)
        # 1.判断是否为空
        if self.head == None:
            self.head = n
            self.head.next = self.head
        else:
            cur = self.head
            # 遍历到最后一个节点
            while cur.next != self.head:
                cur = cur.next
            # cur现在指向最后一个节点
            # cur.next = n
            # n.next = self.head
            n.next = cur.next 
            cur.next = n
    
    
    # insert(pos, item) 指定位置添加元素     
    # 假设pos的位置是合法的，即pos in (0, link.length())之间
    def insert(self, pos, item):
        n = Node(item)  # 创建节点
        
        # 1. 判断链表是否为空
        if self.head == None:
            print("链表为空")
            self.head = n
            n.next = self.head 
            
        else:    
            # 2. 插入在第一个节点
            if pos == 0:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next 
                n.next = self.head 
                cur.next = n
                self.head = n
            # 3. 插入在中间节点或者尾部节点
            else:
                cur = self.head 
                for i in range(pos-1):
                    cur = cur.next
                n.next = cur.next 
                cur.next = n
    
    # remove(item) 删除节点
    def remove(self, item):
        # 1. 判断链表是否为空
        if self.head == None:
            print("链表为空")
            return False
        # 2. 链表不为空
        else:
            # 2.1 删除的节点是第一个节点
            if self.head.data == item:
                # 2.1.1 链表只有一个节点
                if self.head.next == self.head:
                    self.head = None 
                # 2.1.2 链表不止一个节点
                else:
                    cur = self.head 
                    while cur.next != self.head:
                        cur = cur.next 
                    cur.next = self.head.next 
                    self.head = self.head.next 
            # 删除的节点是中间节点或者最后一个节点
            else:

                cur = self.head 
                pre = None 
                # 遍历节点, 若找到了节点，则return
                while cur.next != self.head:
                    if cur.data == item:
                        pre.next = cur.next 
                        return 
                    else:
                        pre = cur
                        cur = cur.next 
                        
                # cur现在指向最后一个节点
                if cur.data == item:
                    pre.next = cur.next 
                else:
                    print("删除的元素不在链表节点中")
            
    # find(item) 查找节点是否存在
    def find(self, item):
        if self.head == None:
            print("链表为空，查找不到节点")
            return False
        else:
            count = 0
            cur = self.head 
            while cur.next != self.head:
                if cur.data == item:
                    print("节点在链表中，在{0}位置".format(count))
                    return True
                else:
                    count += 1
                    cur = cur.next 
            if cur.data == item:
                count += 1
                print("节点在链表中，在{0}位置".format(count))
            else:
                print("未存在item在节点中")
                    
                
                

    
if __name__ == "__main__":
    csl = circleSingleLink()
    csl.addInHead(2)
    csl.addInHead(4)
    csl.append(5)
    csl.insert(0,6)
    csl.insert(1,10)
    csl.items()
    csl.find(5)
    
    csl.remove(5)
    
    csl.items()

        
            
            
        
                   
        

    
    
        
        
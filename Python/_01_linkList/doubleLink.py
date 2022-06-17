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

class node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.pre = None
        self.next = None

class dobuleLink(object):
    def __init__(self) -> None:
        self.head = None
    
    # 创建链表
    def create(self, item):
        headNode = node(item)
        self.head = headNode
    
    # is_empty() 链表是否为空
    def is_empyt(self):
        if self.head == None:
            print("双向链表为空")
        else:
            print("双向链表不为空")
    
    # length() 链表长度
    def length(self):
        cur = self.head 
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        print("双向链表的长度为{0}".format(count))
        
    # items() 获取链表数据迭代器
    def items(self):
        if self.head == None:
            print("双向链表为空")
            return 
        else:
            itemsList = []
            cur = self.head
            while cur != None:
                itemsList.append(cur.data)
                cur = cur.next
            print("双向链表的data迭代器为：{0}".format(itemsList))
            
    # add(item) 链表头部添加元素
    def addHead(self, item):
        n = node(item)
        if self.head == None:
            print("双向链表为空")
            self.head = n
        else:
            n.next = self.head
            self.head.pre = n
            self.head = n
    
    # append(item) 链表尾部添加元素
    def appendTail(self, item):
        n = node(item)
        if self.head == None:
            print("双向链表为空")
            self.head = n
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = n
            n.pre = cur
            
    # insert(pos, item) 指定位置添加元素
    def insert(self, pos, item):
        n = node(item)

            
        if self.head == None:  
            print("双向链表为空")      # 在头部添加数据
            self.head = n
                    
        else:                   # 双向链表不为空
            cur = self.head 
            count = 0
            while cur != None:
                count += 1
                cur = cur.next
            if pos <= 0:            # 在头部添加节点
                pos.next = self.head 
                self.head = pos
            if pos >= (count -1):   # 在尾部添加node
                cur = self.head 
                while cur.next != None:
                    cur = cur.next
                cur.next = n
                n.pre = cur
            else:                   # 在中间添加数据
                cur = self.head         
                for i in range(pos - 1):
                    cur = cur.next
                n.next = cur.next
                cur.next.pre = n
                cur.next = n
                n.pre = cur
    
    
    # # remove(item) 删除节点
    def remove(self, item):
        # 1. 判断是否为空
        if self.head == None:   # 链表为空
            print("链表为空")
        else:           # 链表不为空
            cur = self.head
            # 2.判断删除的是否为头结点
            if cur.data == item:   # 头结点删除
                if cur.next == None:   # 链表只要一个元素
                    self.head == None
                else:           # 链表不止一个元素
                    self.head = cur.next 
                    cur.next.pre = None
            # 3. 删除的不是头结点
            else:
                while cur != None:
                    if cur.data == item:
                        break
                    else:
                        cur = cur.next
                if cur.next != None:            # 删除的节点是中间节点
                    pre = cur.pre 
                    nextNode = cur.next
                    pre.next = nextNode
                    nextNode.pre = pre
                elif cur.next == None:          #  删除的节点是尾部节点
                    pre = cur.pre 
                    cur.pre = None 
                    pre.next = None
                    
                    
if __name__ == "__main__":
    dl = dobuleLink()
    dl.create(2)
    dl.addHead(3)
    dl.appendTail(5)
    dl.insert(1, 10)
    dl.items()
    dl.remove(10)
    dl.items()
                    

                    
                    
            
                
                    
                
                
                
            
        
        
        
'''
is_empty() 链表是否为空
length() 链表长度
items() 获取链表数据迭代器
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
removeIndex(index, item) 删除指定位置的节点
find(item) 查找节点是否存在
'''

import copy
from re import L

from nbformat import current_nbformat

# 定义节点class
class singleLinkNode(object):
    def __init__(self, data:int) -> None:
        self.data = data
        self.next = None
    



# 定义链表class
class singleLink(object):
    # 初始化链表
    def __init__(self) -> None:
        self.head:singleLinkNode = None
    
    # 创建链表
    def createLink(self, firstNode):
        self.head = firstNode
    
    # is_empty() 链表是否为空
    # 为空则返回0， 不为空则返回1
    def is_empty(self) -> int:
        print("*******is_empty()*********")
        if self.head == None:
            print("链表为空")
            return 0
        else:
            print("链表不为空")
            return 1
    
    # length() 链表长度
    def length(self):
        print("*********length()**********")
        # 判断链表是否为空
        if self.is_empty():
            lengthcout = 0
            current_node = self.head
            while current_node is not None:
                lengthcout += 1
                current_node = current_node.next
            print("链表长度为：", lengthcout)
                
        else:
            print("链表长度为0")
        
    # items() 获取链表数据data迭代器,把所有节点的data放到一个list或者迭代器中
    def items(self):
        print("******* items() ********")
        if self.head == None:
            print("链表为空")
            return 0
        else:
            currentNode = self.head
            datalist = []
            while currentNode is not None:
                datalist.append(currentNode.data)
                currentNode = currentNode.next
            print("数据迭代器为：", datalist)
            return datalist
     
    # add(item) 链表头部添加元素
    def addInHead(self, item:singleLinkNode):
        if self.head == None:
            print("链表为空")
            self.head = item
        else:
            print("链表不为空")
            item.next = self.head
            self.head = item
            
    # append(item) 链表尾部添加元素
    def appendInTail(self, item:singleLinkNode):
        if self.head == None:
            print("链表为空")
            self.head = item 
        else:
            print("链表不为空")
            currentNode = self.head 
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = item
        
    # insert(pos, item) 指定位置添加元素，从0开始
    def insert(self, pos, item):
        countlink = 0
        cur = self.head
        while cur != None:
            countlink += 1
            cur = cur.next
        if pos > countlink:
            print("pos超出链表长度")
        else:
            cur = self.head
            for i in range(pos-1):
                cur = cur.next
        item.next = cur.next
        cur.next = item
        
    # # remove(item) 删除节点
    # def remove(self, item):
    #     if self.head == None:
    #         print("链表为空")
    #         return
    #     pre = self.head
    #     if pre.data == item:    
    #         self.head = pre.next
    #         return 
    #     cur = pre.next 
    #     while cur != None:
    #         if cur.data == item:
    #             pre.next = cur.next
    #         cur = cur.next 
    #         pre = pre.next
    
    
    # remove(item) 删除节点
    def remove(self, item):
        # 1.判断链表是否为空
        if self.head == None:           # 链表为空
            print("链表为空")
        else:           # 链表不为空
            cur = self.head
            # 2. 判断删除的是否为第一个节点,如果是，则删除第一个节点
            if cur.data == item:
                self.head = cur.next
            # 3. 删除的节点不是第一个节点，在内部或者在尾部
            else:
                pre = None 
                while cur != None:
                    if cur.data == item:
                        pre.next = cur.next
                    pre = cur
                    cur = cur.next

    
    # # removeIndex(index, item) 删除指定位置的节点
    # def removeIndex(self, index):
    #     if self.head == None:
    #         print("链表为空")
    #         return
    #     count = 0
    #     cur = self.head 
    #     while cur != None:
    #         count += 1
    #         cur = cur.next
    #     if index > (count - 1):  # 删除最后一个
    #         index = count-1
        
    #     pre = self.head
    #     for i in range(index-1):
    #         pre = pre.next
    #     cur = pre.next
        
    #     pre.next = cur.next
                            
    
    # removeIndex(index) 删除指定位置的节点
    # 假设输入的index的范围在0到len(link)-1之间，不存在无效输入
    def removeIndex(self, index):
        # 1. 判断链表是否为空
        if self.head == None:           # 如果链表为空
            print("链表为空")
        else:                           # 如果链表不为空
            cur = self.head
            # 2. 如果删除的是第一个元素
            if index == 0:
                self.head = cur.next
            # 3. 删除的元素是中间节点或者尾节点
            else:
                pre = None
                for i in range(index):
                    pre = cur
                    cur = cur.next
                pre.next = cur.next
    
    
    
    
    # find(item) 查找节点是否存在
    def find(self, item):
        cur = self.head 
        i = 0
        while cur != None:
            if cur.data == item:
                print("存在节点，在{0}位置".format(i))
                return i
            cur = cur.next
            i = i + 1
        print("不存在节点")
        return -1
        

if __name__ == "__main__":
    singlelink = singleLink()

    n1 = singleLinkNode(2)
    singlelink.createLink(n1)
    
    n2 = singleLinkNode(3)
    singlelink.addInHead(n2)
    
    n3 = singleLinkNode(4)
    singlelink.appendInTail(n3)
    
    n4 = singleLinkNode(5)
    singlelink.insert(3, n4)
    singlelink.removeIndex(0)
    # singlelink.remove(5)
    # singlelink.remove(3)
    singlelink.find(3)
    temp = singlelink.is_empty()

    singlelink.length()
    items = singlelink.items()

    

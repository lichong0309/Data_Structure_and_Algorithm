'''
addNode(item)    给二叉树添加节点
isEmpty()        判断二叉树是否为空
items()          得到整个二叉树的元素迭代器
getDepth()       得到深度
getParent()      得到父节点
getNodeNum()     得到节点数量
clearTree()      清空二叉树
DestoryTree()    销毁二叉树
preOrder()       先序遍历
inOrder()        中序遍历
postOrder()      后序遍历
breadthFirst()   广度优先遍历
search()         查找二叉树元素
remove(item)         删除某一元素
'''

import gc
from typing import *
# 定义节点类
class Node(object):
    def __init__(self, item) -> None:
        self.item = item 
        self.leftNode = None 
        self.rightNode = None 
        
        
        
# 定义二叉树类
class BinaryTree(object):
    def __init__(self) -> None:
        self.root:Node = None
    
    
    # isEmpty()        判断二叉树是否为空
    def isEmpty(self):
        if self.root == None:
            print("二叉树为空")
            return False
        else:
            print("二叉树不为空")
            return True
    
    # addNode(item)    给二叉树添加节点
    def addNode(self, item):
        newNode = Node(item)
        
        # 如果二叉树为空，新节点为root节点
        if self.root == None:
            print("二叉树为空")
            self.root = newNode
            # print("根节点添加成功")
        
        # 如果二叉树不为空    
        else:
            # 对二叉树进行广度优先遍历
            queue = []    # 创建队列
            queue.append(self.root)      # 初始化将根节点加入队列
            # 当队列不为空
            while queue != []:
                cur = queue.pop(0)      # 出队列，作为当前的遍历节点的位置
                # 如果当前节点的左孩子节点为空，则添加新节点到当前节点的左孩子
                # 否则判断当前节点的右孩子节点是否为空
                if cur.leftNode == None:
                    cur.leftNode = newNode
                    # print("节点添加成功")
                    return True
                else:
                    # 如果当前节点的右孩子节点为空，则添加新节点到当前节点的右孩子
                    if cur.rightNode == None:
                        cur.rightNode = newNode
                        # print("节点添加成功")
                        return True
                    # 如果当前节点的左孩子和右孩子都不为空，则继续遍历
                    else:
                        queue.append(cur.leftNode)      # 先添加左孩子到队列
                        queue.append(cur.rightNode)     # 再添加右孩子到队列
                        


    # items()          得到整个二叉树的元素迭代器
    def items(self):
        binaryTreeList = []         # 存放二叉树元素的迭代器
        # 如果二叉树为空
        if self.root == None:
            print("二叉树为空")
            return binaryTreeList
        
        # 如果二叉树不为空
        else:
            # 广度优先遍历，获得二叉树的元素，并存放到binaryTreeList中
            queue = []          # 初始化队列
            queue.append(self.root)
            while queue != []:
                cur = queue.pop(0)
                binaryTreeList.append(cur.item)
                if cur.leftNode != None:
                    queue.append(cur.leftNode)
                else:
                    pass
                if cur.rightNode != None:
                    queue.append(cur.rightNode)
                else:
                    pass
        return binaryTreeList
    
    
    
    # getDepth()       得到深度
    def getDepth(self):
        count = 0
        if self.root == None:
            print("二叉树为空")
            return count
        else:
            cur = self.root
            while cur != None:
                count = count + 1
                cur = cur.rightNode
        return count
    
    
    # getParent()      得到父节点
    # 使用广度优先遍历
    def getParent(self, node):
        if node.item == self.root.item:
            print("节点为根节点，没有父节点")
            return False
        else:
            location = 0        # 父节点的位置
            queue = []
            queue.append(self.root)
            while queue != []:
                cur = queue.pop(0)
                if cur.leftNode.item == node.item or cur.rightNode.item == node.item:
                    pNode = cur
                    print("存在父节点，位置为：",location)
                    return pNode
                else:
                    queue.append(cur.leftNode)
                    queue.append(cur.rightNode)
                location += 1
        
        print("节点没有父节点")
        return False
              
              
    # getNodeNum()     得到节点数量
    # 使用先序遍历, 把整个二叉树遍历一遍，计数变量count记录二叉树的个数
    def getNodeNum1(self, root, count=0):
        if root == None:
            return count
        else:
            count = count + 1
            count = self.getNodeNum(root.leftNode, count)
            count = self.getNodeNum(root.rightNode, count)
        return count
    
    # 使用递归，
    def getNodeNum(self, root):
        if root == None:
            return 0 
        else:
            leftCount = self.getNodeNum(root.leftNode)
            rightCount = self.getNodeNum(root.rightNode)
            return 1 + leftCount + rightCount
            
            

    # # clearTree()      清空二叉树
    # # 使用递归
    # def clearTree(self, root):
    #     if root == None:
    #         return True
    #     else:
    #         self.clearTree(root.leftNode)
    #         self.clearTree(root.rightNode)
    #         if root == self.root:
    #             pass
    #         else:
    #             root = None
                
    #     # root=None 并没有释放内存，所以没有修改self.root的内容
    #     self.root = root
    
    # clearTree()           清空二叉树
    # 使用后序遍历 递归
    def clearTree(self, root):
        if root == None:
            return True
        if root.leftNode == None and root.rightNode == None:
            return True
        else:
            self.clearTree(root.leftNode)
            self.clearTree(root.rightNode)
            
            # 删除节点
            root.leftNode = None
            root.rightNode = None
        
        return True
            
    
    # # DestoryTree()    销毁二叉树
    # # 使用递归，从下往上删除节点，最后删除根节点
    # def DestoryTree(self, root):
    #     # print(self.items())
    #     if root == None:
    #         return True
    #     else:
    #         self.DestoryTree(root.leftNode)
    #         self.DestoryTree(root.rightNode)
    #         root = None
        
    #     # root=None 并没有释放内存，所以没有修改self.root的内容
    #     self.root = root
    #     # del root
    
    
    # DestoryTree()         # 销毁二叉树
    # 使用后序遍历 递归
    def DestoryTree(self, root):
        if root == None:
            return True
        else:
            self.DestoryTree(root.leftNode)
            self.DestoryTree(root.rightNode)
            
            # 删除节点
            root.leftNode = None
            root.rightNode = None 
            
            # 删除根节点
            if root == self.root:
                self.root = None
        
        return True
    
    
    # preOrder()       先序遍历
    def __recursionPreOrder(self, root, result):
        if root == None:
            return
        else:
            result.append(root.item)
            if root.leftNode != None:
                self.__recursionPreOrder(root.leftNode, result)
            if root.rightNode != None: 
                self.__recursionPreOrder(root.rightNode, result)
        
    def proOrder(self):
        result = []
        self.__recursionPreOrder(self.root, result)
        print("先序遍历结果：",result)
        
    
    # inOrder()        中序遍历   
    def __recursionInOrder(self, root, result):
        if root == None:
            return 
        else:
            if root.leftNode != None:
                self.__recursionInOrder(root.leftNode, result)
            
            result.append(root.item)
            
            if root.rightNode != None:
                self.__recursionInOrder(root.rightNode, result)
                
                
    def inOrder(self):
        result = []
        self.__recursionInOrder(self.root, result)
        print("中序遍历的结果：", result)


    # postOrder()      后序遍历
    def __recursionPostOrder(self, root, result):
        if root == None:
            return 
        else:
            if root.leftNode != None:
                self.__recursionPostOrder(root.leftNode, result)
            
            if root.rightNode != None:
                self.__recursionPostOrder(root.rightNode, result)
            
            result.append(root.item)
    
    def postOrder(self):
        result = []
        self.__recursionPostOrder(self.root, result)
        print("后序遍历结果：",result)
                     

    # breadthFirst()   广度优先遍历
    def breadthFirst(self):
        if self.root == None:
            print("二叉树为空！")
            return False
        else:
            result = []
            queue = []          # 初始化为空队列
            queue.append(self.root)
            while queue != []:
                cur = queue.pop(0)      # 出队列
                result.append(cur.item)
                if cur.leftNode != None:
                    queue.append(cur.leftNode)
                if cur.rightNode != None:
                    queue.append(cur.rightNode)
        
        print("层序遍历结果：", result)
    
    
    # 前序遍历查找
    def __preSearch(self, root, item, flag, location):
        # root: 子树（树）的根节点
        # item: 需要查找的元素
        # flag：标志是否找到元素，如果找到了则标记1，没有找到则标记为0
        # location: 元素所在的位置
        if root == None:
            return flag, location 
        
        else:
            if root.item == item:
                flag = 1       # flag标记为1
                print("前序遍历查找，元素所在的位置为：",location)
                return flag, location
            else:
                location = location + 1
                flag, location = self.__preSearch(root.leftNode, item, flag, location)
                flag, location = self.__preSearch(root.rightNode, item, flag, location)
                return flag, location 
        
    # 中序遍历查找
    def __inSearch(self, root, item, flag, location):
        # root: 子树（树）的根节点
        # item: 需要查找的元素
        # flag：标志是否找到元素，如果找到了则标记1，没有找到则标记为0
        # location: 元素所在的位置
        
        if root == None:
            return flag, location 
        else:
            if root.leftNode != None:
                flag, location = self.__inSearch(root.leftNode, item, flag, location)
            
            if root.item == item:
                flag = 1        # flag标记为1
                print("中序遍历查找，元素所在位置为：", location)
                return flag, location
            
            location = location + 1
            
            if root.rightNode != None:
                flag, location = self.__inSearch(root.rightNode, item, flag, location) 
                   
            return flag, location 
    
    # 后序遍历查找元素
    def __postSearch(self, root, item, flag, location):
        # root: 子树（树）的根节点
        # item: 需要查找的元素
        # flag：标志是否找到元素，如果找到了则标记1，没有找到则标记为0
        # location: 元素所在的位置     
        if root == None:
            return flag, location 
        else:
            if root.leftNode != None:
                flag, location = self.__postSearch(root.leftNode, item, flag, location)
            if root.rightNode != None:
                flag, location = self.__postSearch(root.rightNode, item, flag, location)
            if root.item == item:
                flag = 1
                print("后序遍历查找，元素所在的位置为：",location)
                return flag, location 
            location = location + 1
            return flag, location 
        
    # 广度优先遍历查找       
    def __breadthSearch(self, item):
        # root: 子树（树）的根节点
        # item: 需要查找的元素
        # flag：标志是否找到元素，如果找到了则标记1，没有找到则标记为0
        # location: 元素所在的位置    
        queue = []
        queue.append(self.root)
        location = 0
        while queue != []:
            cur = queue.pop(0)
            if cur.item == item:
                print("广度优先遍历查找，元素所在的位置为：", location)
                return True
            else:
                if cur.leftNode != None:
                    queue.append(cur.leftNode)
                if cur.rightNode != None:
                    queue.append(cur.rightNode)
            location = location + 1
                    
    
    # search()         查找二叉树元素
    def search(self, item, method="pre"):
        # 前序遍历
        if method == "pre":
            flag, _ = self.__preSearch(self.root, item, flag=0, location=0)
            if flag == 0:
                print("元素不在二叉树中")
        # 中序遍历
        if method == "in":
            flag, _ = self.__inSearch(self.root, item, flag=0, location=0)
            if flag == 0:
                print("元素不在二叉树中")
        # 后序遍历
        if method == "post":
            flag, _ = self.__postSearch(self.root, item, flag=0, location=0)
            if flag == 0:
                print("元素不在二叉树中")
        
        # 广度优先遍历
        if method == "breadth":
            self.__breadthSearch(item)

    # # 前序遍历 删除 
    # def __preRemove(self, root, item, flag):
    #     # root: 子树（树）的根节点
    #     # item: 需要删除的元素的数据
    #     # falg: 删除是否成功的标志， 0表示删除失败，1表示删除成功
    #     if root == None:
    #         return flag
        
    #     else:
    #         # cur = root
    #         # 是否存在元素item
    #         if root.item == item:
    #             while root != None:
    #                 print("test")
    #                 # 判断是否为叶节点
    #                 if root.leftNode == None and root.rightNode == None:          # 为叶节点
    #                     root = None                # 直接删除节点
    #                 else:                           # 不为叶节点
    #                     if root.leftNode != None:
    #                         root.item = root.leftNode.item
    #                         root = root.leftNode
    #                     else:
    #                         if root.rightNode != None:
    #                             root.item = root.rightNode.item
    #                             root = root.rigthNode
    #             flag = 1                # 标志设为1，表示删除成功
    #             print("删除成功")
    #             return flag
    #         # 迭代
    #         if root.leftNode != None:
    #             flag = self.__preRemove(root.leftNode, item, flag)
    #         if root.rightNode != None:
    #             flag = self.__preRemove(root.rightNode, item, flag)

    #     # self.root = root 
    #     return flag
    
    
    # def __preRemove(self, root, item, flag):
    #     if root == None:
    #         return flag 
    #     if root.item == item:
    #         # 是叶节点
    #         if root.leftNode == None and root.rightNode == None:
    #             root = None
    #             flag = 1
    #         # 非叶节点
    #         else:
    #             if root.leftNode != None:
    #                 root.item, root.leftNode.item = root.leftNode.item, root.item
    #             else:
    #                 root.item, root.rightNode.item = root.rightNode.item, root.item
            
            
    #     if root != None:
    #         flag = self.__preRemove(root.leftNode, item, flag)
    #         flag = self.__preRemove(root.rightNode, item, flag)
        
    #     self.root = root
    #     return flag 
    
    
    # 前序遍历删除
    def __preRemove(self, root, item, flag=0):
        # root: 子树（树）的根节点
        # item: 需要删除的元素的数据
        # falg: 删除是否成功的标志， 0表示删除失败，1表示删除成功  
    
        # 如果删除的是根节点
        if self.root.item == item:
            cur = self.root
            while cur != None:
                # 1. 如果存在左孩子：
                if cur.leftNode != None:
                    cur.item = cur.leftNode.item        # 覆盖root节点的数据
                    
                    # 1.1 如果子节点为叶节点，则直接删除子节点
                    if cur.leftNode.leftNode == None and cur.leftNode.rightNode == None:
                        cur.leftNode = None
                        flag = 1
                        return flag
                    # 1.2 如果子节点不是叶节点：
                    else:
                        cur = cur.leftNode
                # 2. 如果没有左孩子，有右孩子
                if cur.leftNode == Node and cur.rightNode != None:
                    cur.item = cur.rightNode.item       # 覆盖root节点的数据
                    
                    # 2.1 如果子节点为叶节点，则直接删除子节点
                    if cur.rightNode.leftNode == None and cur.rightNode.rightNode == None:
                        cur.rightNode = None
                        flag = 1
                        return flag
                    # 2.2 如果子节点不是叶子节点
                    else:
                        cur = cur.rightNode
                
                # 3. 如果左孩子和右孩子都没有：
                if cur.leftNode == None and cur.rightNoe == None:
                    self.root = None
                    flag = 1
                    return flag 
        # 如果删除的不是根节点
        if self.root.item != item:
            if root == None:
                return flag 
            
            # 如果父节点的左孩子是应该删除的节点
            if root.leftNode != None and root.leftNode.item == item:

                # # 1. 如果该删除的节点是叶子节点，直接删除
                # if root.leftNode.leftNode == None and root.leftNode.rightNode == None:
                #     root.leftNode = None
                # # 2. 如果删除的节点不是叶子节点，则需要调整二叉树的结构
                # else:
                #     cur = root
                #     while cur != None:
                #         # 2.1 如果root.leftNode的左孩子存在
                #         if root.leftNode.leftNode != None:
                cur = root
                while cur != None:
                    # 1. 如果root.leftNode 有左孩子：
                    if cur.leftNode.leftNode != None:
                        cur.leftNode.item = cur.leftNode.leftNode.item 
                        # 1.1 如果root.leftNode的左孩子是叶子节点, 则直接删除
                        if cur.leftNode.leftNode.leftNode == None and cur.leftNode.leftNode.rightNode == None:
                            cur.leftNode.leftNode = None
                            flag = 1 
                            return flag
                        # 1.2 如果root.leftNode的左孩子不是叶子节点
                        else:
                            cur = cur.leftNode
                    # 2. 如果root.leftNode没有左孩子，但是有右孩子
                    if cur.leftNode.leftNode == None and cur.leftNode.rightNOde != None:
                        cur.leftNode.item = cur.leftNode.rightNode.item
                        # 2.1 如果root.leftNode的右孩子是叶子节点，则直接删除
                        if cur.leftNode.rightNode.leftNode == None and cur.leftNode.rightNode.rightNode == None:
                            cur.leftNode.rightNode = None 
                            flag = 1
                            return flag 
                        #2.2 如果root.leftNode.rightNode不是叶子节点
                        else:
                            cur = cur.leftNode
                    # 3. 如果root.leftNode没有左孩子和右孩子，则直接删除
                    else:
                        cur.leftNode = None
                        flag = 1 
                        return flag 
                    
            # 如果父节点的右孩子是应该删除的节点
            if root.rigthNode != None and root.rightNode.item == item:
                cur = root
                while cur != None:
                    # 1. 如果root.rightNode 有左孩子：
                    if cur.rightNode.leftNode != None:
                        cur.rightNode.item = cur.rightNode.leftNode.item 
                        # 1.1 如果root.rightNode的左孩子是叶子节点, 则直接删除
                        if cur.rightNode.leftNode.leftNode == None and cur.rightNode.leftNode.rightNode == None:
                            cur.rightNode.leftNode = None
                            flag = 1 
                            return flag
                        # 1.2 如果root.rightNode的左孩子不是叶子节点
                        else:
                            cur = cur.rightNode
                    # 2. 如果root.rightNode没有左孩子，但是有右孩子
                    if cur.rightNode.leftNode == None and cur.rightNode.rightNOde != None:
                        cur.rihgtNode.item = cur.rightNode.rightNode.item
                        # 2.1 如果root.rightNode的右孩子是叶子节点，则直接删除
                        if cur.rightNode.rightNode.leftNode == None and cur.rightNode.rightNode.rightNode == None:
                            cur.rightNode.rightNode = None 
                            flag = 1
                            return flag 
                        #2.2 如果root.rightNode.rightNode不是叶子节点
                        else:
                            cur = cur.rightNode
                    # 3. 如果root.leftNode没有左孩子和右孩子，则直接删除
                    else:
                        cur.leftNode = None
                        flag = 1 
                        return flag 
            
            flag = self.__preRemove(root.leftNode, item, flag)
            flag = self.__preRemove(root.rightNode, item, flag)
            
            return flag 
                    

    # remove(item)         删除某一元素
    def remvoe(self, item, method:str):
        if method == "pre":
            flag = self.__preRemove(self.root, item, flag=0)
            if flag == 0:
                print("所删除的元素不在二叉树中")

        
        

if __name__ == "__main__":
    bt = BinaryTree()
    bt.isEmpty()
    bt.addNode(10)
    bt.addNode(100)
    bt.addNode(200)
    bt.addNode(300)
    bt.addNode(400)
    bt.addNode(500)
    
    items = bt.items()
    print(items)
    
    # 寻找父节点
    bt.getParent(Node(100))
    
    # 得到节点数量
    count = bt.getNodeNum(bt.root)
    print("节点的数量为：", count)
    
    # bt.clearTree(bt.root)
    # bt.DestoryTree(bt.root)
    
    # bt.isEmpty()
    # items = bt.items()
    # print(items)
    
    
    # 前序遍历 
    bt.proOrder()
    
    # 中序遍历
    bt.inOrder()
    
    # 后序遍历
    bt.postOrder()
    
    # 层序遍历
    bt.breadthFirst()
    
    
    # 前序遍历查找
    # bt.search(400,"breadth")
    
    # 前序遍历删除
    bt.remvoe(100, "pre")
    bt.proOrder()
    items = bt.items()
    print(items)
        

    
        
                        
                    
                
                    
                    
                    
                
            

















'''
addNode(item)    给二叉树添加节点
isEmpty()        判断二叉树是否为空
items()          得到整个二叉树的元素迭代器
getDepth()       得到深度
clearTree()      清空二叉树
DestoryTree()    销毁二叉树
preOrder()       先序遍历
inOrder()        中序遍历
postOrder()      后序遍历
breadthFirst()   广度优先遍历
search()         查找二叉树元素
remove(item)         删除某一元素
'''


# 定义节点类

from cgitb import reset


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
            print("根节点添加成功")
        
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
                    print("节点添加成功")
                    return True
                else:
                    # 如果当前节点的右孩子节点为空，则添加新节点到当前节点的右孩子
                    if cur.rightNode == None:
                        cur.rightNode = newNode
                        print("节点添加成功")
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
    
    # clearTree()      清空二叉树
    # 使用递归
    def clearTree(self, root):
        if root == None:
            return True
        else:
            self.clearTree(root.leftNode)
            self.clearTree(root.rightNode)
            if root == self.root:
                pass
            else:
                root = None
                
        # root=None 并没有释放内存，所以没有修改self.root的内容
        self.root = root
            
    
    # DestoryTree()    销毁二叉树
    # 使用递归，从下往上删除节点，最后删除根节点
    def DestoryTree(self, root):
        # print(self.items())
        if root == None:
            return True
        else:
            self.DestoryTree(root.leftNode)
            self.DestoryTree(root.rightNode)
            root = None
        
        # root=None 并没有释放内存，所以没有修改self.root的内容
        self.root = root
        # del root
    
    
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

    
    # remove(item)         删除某一元素
    def remvoe(self, item):
        pass
        

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
    bt.search(400,"post")
    

    
        
                        
                    
                
                    
                    
                    
                
            













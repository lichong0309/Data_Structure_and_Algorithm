'''
addNode(item)    给二叉树添加节点
isEmpty()        判断二叉树是否为空
items()          得到整个二叉树的元素迭代器
getDepth()       得到深度
getParent(item)  得到父节点
getNodeNum()     得到节点数量
clearTree()      清空二叉树
DestoryTree()    销毁二叉树
preOrder()       先序遍历
inOrder()        中序遍历
postOrder()      后序遍历
breadthFirst()   广度优先遍历
search(item)     查找二叉树元素
remove(item)     删除某一元素
'''


# 节点
class Node(object):
    def __init__(self, item) -> None:
        self.item = item 
        self.leftNode = None
        self.rightNode = None
         

# binarySearchTree
class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None
        
    # isEmpty()        判断二叉树是否为空
    def isEmpyt(self):
        if self.root == None:
            print("二叉树为空")
            return False
        else:
            print("二叉树不为空")
            return True
    
    
    # addNode(item)    给二叉树添加节点
    # 递归
    def addNode(self, root, item):
        # 退出标志
        if root == None:
            root = Node(item)
            print("添加节点成功")
            return True
        else:
            if item == root.item:
                print("原二叉树中已有节点")
                return True
            elif item < root.item:
                self.addNode(root.leftNode, item)
            elif item > root.item:
                self.addNode(root.rightNode, item)
                
    
    # items()          得到整个二叉树的元素迭代器
    def items(self):
        pass

    
    # getDepth()       得到深度
    def getDepth(self):
        pass
    
    # getParent()      得到父节点
    def getParent(self, item):
        pass
    
    
    # getNodeNum()     得到节点数量
    def getNodeNum(self):
        pass
    
    # clearTree()      清空二叉树
    def clearTree(self):
        pass
    
    # DestoryTree()    销毁二叉树
    def DestoryTree(self):
        pass
    
    
    # preOrder()       先序遍历
    def preOrder(self):
        pass
    
    # inOrder()        中序遍历
    def inOrder(self):
        pass
    
    # postOrder()      后序遍历
    def postOrder(self):
        pass
    
    
    # breadthFirst()   广度优先遍历
    def breadthFirst(self):
        pass
    
    
    # search()         查找二叉树元素
    def search(self, item):
        pass
    
    
    # remove(item)         删除某一元素
    def remove(self, item):
        pass
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
    
    # 


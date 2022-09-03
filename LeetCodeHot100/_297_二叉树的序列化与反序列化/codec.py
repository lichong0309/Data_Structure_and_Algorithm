'''
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

示例 1：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：

输入：root = [1,2]
输出：[1,2]
 

提示：

树中结点数在范围 [0, 104] 内
-1000 <= Node.val <= 1000
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def bfs(self, root):
        res = []            # 存放二叉树节点的list
        if root == None:
            return "None"
        queue = []
        queue.append(root)
        while queue != []:
            cur = queue.pop(0)
            if cur == None:
                res.append('None')
            else:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
        return ",".join(res)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 层序遍历：
        res = self.bfs(root)
        # print(res)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dataList = data.split(',')
        if dataList[0] == "None":
            return []
        else:
            newTree = TreeNode(int(dataList[0]))
            queue = []
            queue.append(newTree)
            i = 1
            while queue != [] and i < len(dataList):
                cur = queue.pop(0)
                # 左孩子
                if dataList[i] == "None":
                    pass
                else:
                    tempNode = TreeNode(int(dataList[i]))
                    cur.left = tempNode
                    queue.append(cur.left)
                i = i + 1
                # 右孩子
                if dataList[i] == "None":
                    pass
                else:
                    tempNode = TreeNode(int(dataList[i]))
                    cur.right = tempNode
                    queue.append(cur.right)
                i = i + 1

        return newTree
                    
                
             

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
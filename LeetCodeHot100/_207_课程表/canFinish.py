'''
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
 

提示：

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同
'''

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 使用拓扑图
        # 1. 创建拓扑图和每个节点的入度
        # 2. 深度优先遍历，

        # 初始化
        adj = [[] * numCourses for _ in range(numCourses)]  # 邻接矩阵
        inDeg = [0] * numCourses                            # 存放每个节点当前的入度

        # 1. 创建拓扑图
        for i in range(len(prerequisites)):
            preList= prerequisites[i]
            starNode = preList[0]
            endNode = preList[1]
            adj[starNode].append(endNode)           # 添加后驱节点
            inDeg[endNode] += 1                     # 将后驱节点的入度加1

        # 记录所有入度为0的节点
        queue = []      # 存放入度为0的节点
        for i in range(len(inDeg)):
            if inDeg[i] == 0 :
                queue.append(i)

        # 深度优先遍历
        while queue != []:
            numCourses -= 1
            cur = queue.pop(0)          
            cur_adj = adj[cur]          # 邻接节点的list
            # 更新入度
            for i in range(len(cur_adj)):
                inDeg[cur_adj[i]] -= 1
                if inDeg[cur_adj[i]] == 0:
                    queue.append(cur_adj[i])
                else:
                    pass

        ans = False
        if numCourses == 0:
            ans = True 
        else:
            pass
        return ans
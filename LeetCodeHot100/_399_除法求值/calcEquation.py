'''
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
 

提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成

'''

class Solution:
    def createGraph(self, equations, values):
        # 创建图
        # graph:{key, value} -> dic
        # key:str           表示一个起始节点
        # value:{key, value}   表示一个节点到另外一个节点key的权重value
        graph = {}

        for (x,y), z in zip(equations, values):
            # 如果起始节点x已经在graph中,则直接添加y节点的权重
            if x in graph:
                graph[x][y] = z
            # 如果起始节点x不在graph中，则添加x节点，并且添加x到y节点的权重
            else:
                graph[x] = {y:z}
            # 如果结束节点y已经在graph中， 则反向添加y到起始节点x的权重，为倒数
            if y in graph:
                graph[y][x] = 1/z
            # 如果结束节点y不在graph中，则添加y节点，并且添加y到x节点的权重，为倒数
            else:
                graph[y] = {x:1/z}
        return graph
        
    def dfs(self, x, y, graph, visted):
        # 1. 判断起始节点x是否在graph中
        # 1.1 如果不在，则直接返回-1.0
        if x not in graph:
            return -1.0
        # 1.2 如果起始节点x在graph中
        else:
            # 1.2.1 如果起始节点和结束节点相同，则返回1.0
            if x == y:
                return 1.0
            # 如果起始节点和结束节点不相同，则使用递归进行深度优先搜索
            else:
                for node in graph[x]:
                    if node == y:
                        return graph[x][y]
                    else:
                        # 如果node不在visted中，则可以继续遍历
                        if node not in visted:
                            visted.add(node)         # 将node添加到visted表示已经访问
                            temp = self.dfs(node, y, graph, visted)    # 递归
                            # 如果temp不为-1，则说明这条遍历的路径有可能得到目标结果
                            if temp != -1.0:
                                return temp * graph[x][node]
                            else:
                                pass
        return -1.0


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 使用并查集，创建图，进行深度优先搜索
        # 创建图
        ans = []
        graph = self.createGraph(equations, values)
        for (x,y) in queries:
            visted = set()              # 添加已经访问的节点，避免重复访问
            ans.append(self.dfs(x, y, graph, visted))

        return ans 

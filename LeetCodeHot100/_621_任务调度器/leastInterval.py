import collections
class Solution:
    def leastInterval(self, tasks, n):

        # 生成字典dic{key,value}
        # key: 某种任务种类 “A”:char
        # vlaue: 某种任务的数量  10：int
        dic = collections.Counter(tasks)        # 生成字典dic{key,value}

        
        # 1为初始化冷却时间
        for key, value in dic.items():
            dic[key] =  [value, 1]
            
        taskNum = len(dic)                      # 生成的dic的长度，即任务类型的数量
        
        # dictory to list -> List[tuple(char, List[int, int])]
        dicSort = list(dic.items())
        # list中的tuple to list -> List[char, List[int, int]]
        for m in range(taskNum):
            dicSort[m] = list(dicSort[m])      
        
        i = 0           # 控制变量，使得每个任务都能执行，当i=len(tasks)-1时，所有任务都执行完成
        time = 0        # 结果

        while i < len(tasks):
            # 按照dicSort的第二个元素进行排序，从大到小
            dicSort = sorted(dicSort, key=lambda x:[x[1],x[0]], reverse=True)

            # 判断最大值是否处在冷却时间
            for m in range(taskNum):   
                if dicSort[m][1][1] > 0 and dicSort[m][1][0] > 0:            # 不处于冷却时间
                    print("test:", dicSort[m][1][0])
                    # 先修改参数
                    dicSort[m][1][1] = -n           # 重置冷却时间
                    dicSort[m][1][0] -= 1           # 减少任务类型的数量
                    i += 1                         # i ++
                    break                        # 找到了最大值，则break出循环
                       
            time = time + 1

            # 更新冷却时间
            for m in range(taskNum):
                dicSort[m][1][1] += 1
                
        print(time)
        return time
    
cl = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
cl.leastInterval(tasks, n)



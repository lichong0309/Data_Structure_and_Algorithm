from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # ans = []

        # # dic = {key:value}
        # # key: 将k_i作为字典的建
        # # value: [list]: 将相同的k_i 放到一个list中进行保存
        # dic = {}

        # # 先对people进行 倒序 排序：
        # # 后续字典中value:list中的元素就是顺序的
        # people.sort(reverse=True)

        # # 创建字典
        # for sub_p in people:
        #     if sub_p[1] in dic:
        #         dic[sub_p[1]].append(sub_p[0])
        #     else:
        #         dic[sub_p[1]] = [sub_p[0]]

        # # 对dic按照key进行排序,返回list
        # keyList = sorted(dic)

        # # 根据key，从小到大遍历字典dic的每个元素
        # for key in keyList:
        #     value = dic[key]

        #     # 遍历value中的每个元素
        #     for sub_val in value:
        #         count = 0         # 记录比当前值sub_val大于或等于的数量
        #         i = 0             # 循环ans
        #         # 找到sub_val应该插入ans的位置
        #         while count < key and i < len(ans):
        #             if ans[i][0] >= sub_val:
        #                 count = count + 1
        #             else:
        #                 pass
        #             i = i + 1
        #         # i 的位置即为sub_val插入的位置
        #         ans.insert(i, [sub_val, key])

        # people = ans 
        
        # return people


        people = sorted(people, key=lambda x: [x[0],-x[1]],reverse=True)

        ans = []
        for p in people:
            ans.insert(p[1], p)
        people = ans 
        return people

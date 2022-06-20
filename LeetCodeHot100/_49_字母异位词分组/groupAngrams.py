from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # dic:{key,value}
        # key: 字符串按照从小到大的顺序排序后的字符串
        # value: List[str], 相同hash的字符串组成的list
        dic = {}

        ans = []
        for word in strs:
            newStr = ''.join(sorted(word))      # 使用sorted可以作用在string，并且返回副本

            # 如果newStr在dic中已经存在key
            if newStr in dic:
                dic[newStr].append(word)
            # 如果newStr不在dic的key中
            else:
                dic[newStr] = [word]
            
        for key, value in dic.items():
            ans.append(value)

        return ans
    
    
    
    
# class Solution:
#     def groupAnagrams(self, strs):
#         if len(strs) == 0:
#             return [[""]]
#         else:
#             ans = []
#             # {count:[[],[]]}
#             dic = {}

#             # 计算列表中每个元素的ASCII的值
#             for i in range(len(strs)):
#                 count = 0 
#                 for j in strs[i]:
#                     count = count + ord(j)

#                 # 如果字典中已经存在ASCII的值
#                 # 判断strs[i]在什么位置
#                 if count in dic:
#                     flag = 0          # 判断strs[i]是否找到应该插入位置的标志，0表示没有，1表示找到了
#                     # 遍历dic[count]中每个子list
#                     for m in dic[count]:
#                         temp = m[0]     # 随机选择子list中的一个元素
#                         # 判断子list中的元素和strs[i]的元素是否相同
#                         if len(temp) == len(strs[i]):
#                             flag_1 = 0   # 判断temp和strs[i]中元素是否全部相当，0表示全部相等，1表示不全部相等
#                             for w in temp:
#                                 if w not in list(strs[i]):
#                                     flag_1 = 1
#                                 else:
#                                     pass
#                             if flag_1 == 0:         # 如果temp和strs[i]全部相等
#                                 m.append(strs[i])
#                                 flag = 1
#                                 break       # strs[i]找到了位置，则退出对每个子list的循环
#                             else:           # 如果temp和strs[i]不全部相等
#                                 pass
#                         else:       # temp和strs[i]的长度都不相同，直接pass
#                             pass

#                     if flag == 1:       # 找到了位置
#                         pass
#                     else:               # 没有找到位置
#                         dic[count].append([strs[i]])     # 则开辟新的子list给strs[i]
                
#                 # 如果字典中不存在ASCII的值        
#                 else:       
#                     dic[count] = [[strs[i]]]             # 则开辟新的子list给strs[i]
            
#             for key, value in dic.items():
#                 for sub_list in value:
#                     ans.append(sub_list)
        
#             return ans

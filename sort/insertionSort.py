# -*- coding: UTF-8 -*-
from typing import List
class insertionSort(object):
    def __init__(self, item):
        self.item = item

    def sort(self):
        length = len(self.item)
        
        # i: 循环的轮数，从1开始
        # j: 每次循环比较的次数
        for i in range(1, length):
            j = i - 1
            temp = self.item[i]
            while j >= 0:
                if self.item[j] > temp:
                    self.item[j+1] = self.item[j]
                    j = j -1
                else:
                    break
            self.item[j+1] = temp
            
            
    def sort2(self):
        length = len(self.item)
        # i: 循环的轮数，从1开始
        # j: 每轮比较的索引的范围， [i-1, 0]
        for i in range(1,length):
            for j in range(i, 0, -1):
                if self.item[j] < self.item[j-1]:
                    self.item[j], self.item[j-1] = self.item[j-1], self.item[j]
                else:
                    break
                    
            
if __name__ == "__main__":
    import numpy as np   
    import copy
    
    randomItem = np.random.randint(100, size=5).tolist()
    objItem = copy.deepcopy(randomItem)
    
    s = insertionSort(objItem)
    print("排序前：", s.item)
    s.sort2()
    print("排序后：", s.item)

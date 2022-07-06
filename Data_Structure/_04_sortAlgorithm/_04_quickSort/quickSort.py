'''
冒泡排序    bubbleSort()
选择排序    selectionSort()
插入排序    insertionSort()
希尔排序    shellSort()
归并排序    mergeSort()
快速排序    quickSort()
堆排序      heapSort()
基数排序    radixSort()
计数排序    countingSort()
桶排序      buckerSort()
'''
from typing import List
class quickSort(object):
    def __init__(self, item) -> None:
        self.item = item
    
    def sort(self, left, right):
        # left: 起始索引
        # right: 结束索引
        
        # 递归结束的标志
        if left >= right:
            return 
        else:
            pivot = self.item[left]         # 定义标准元素
            i = left                        # 定义左边的起始元素
            j = right                       # 定义右边的起始元素
            
            # 左右元素开始寻找符合的元素
            while i < j:
                # 如果标准元素在两头，则从远离标准元素的一头开始循环，比如本例中是从j开始循环，之后是i循环
                # 防止【19， 75， 70】这样的情况发生
                while self.item[j] >= pivot and i < j:
                    j = j - 1 
                
                while self.item[i] <= pivot and i < j:
                    i = i + 1

                # 如果没有i和j没有重合，则交换元素位置
                if i < j:
                    self.item[i], self.item[j] = self.item[j], self.item[i]
            # 基准元素交换位置
            self.item[left], self.item[i] = self.item[i], self.item[left]
        
        self.sort(left, i-1)
        self.sort(i+1, right)
                    
                    
if __name__ == "__main__":
    import numpy as np   
    import copy
    
    randomItem = np.random.randint(100, size=10).tolist()
    objItem = copy.deepcopy(randomItem)
    
    s = quickSort(objItem)
    print("排序前：", s.item)
    s.sort(0, (len(objItem)-1))
    print("排序后：", s.item)

          
                
                    
            
        
        


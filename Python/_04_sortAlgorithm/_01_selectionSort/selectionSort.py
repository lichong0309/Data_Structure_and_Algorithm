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
class selectionSort(object):
    def __init__(self, item:List[int]) -> None:
        self.item = item
        
    def sort(self):
        # i: 循环次数(从0开始)
        #    需要循环len(self.item)次，因为每次循环只选择self.item中最小的一个元素，所以需要循环len(self.item)次
        #    因为最后一次循环只剩下一个元素了，不需要比较，所以也可以一共循环len(self.item) - 1次
        # j: 每次循环的比较次数
        #    每次循环比较的索引为 [i+1, len(self.item)-1], 即range(i+1, len(self.item))
        
        
        length = len(self.item)
        for i in range(length):
            minIndex = i        # 初始化最小数据的索引
            for j in range(i+1, length):
                if self.item[j] < self.item[minIndex]:
                    minIndex = j
                else:
                    pass
            # 数值最小的节点与循环节点交换位置
            if minIndex != i:
                self.item[i], self.item[minIndex] = self.item[minIndex], self.item[i]

    # 改进
    def sortOpt(self):
        # i: 循环的轮次（从0开始) = len(self.item) // 2
        # j: 每次循环的索引范围 [i, len(self.item)-1-i], 即：range(i, len(self.item)-i)
        length = len(self.item)
        for i in range(length//2):
            # 初始化最大值和最小值的索引
            minIndex = i
            maxIndex = length-1-i
            for j in range(i, length-i):
                # 找出最大值的索引
                if self.item[j] > self.item[maxIndex]:
                    maxIndex = j
                else:
                    pass
                # 找出最小值的索引
                if self.item[j] < self.item[minIndex]:
                    minIndex = j
                else:
                    pass
 
            if minIndex != i:
                if maxIndex != i:           # 最大值不是索引为i的元素，就可以直接交换
                    self.item[i], self.item[minIndex] = self.item[minIndex], self.item[i]
                else:                       # 最大值是索引为i的元素，不可以直接交换
                    maxIndex = minIndex     # 更改maxIndex的索引
                    self.item[i], self.item[minIndex] = self.item[minIndex], self.item[i]
                    
            if maxIndex != length-1-i:        
                # 交换maxIndex和length-1-i的值
                self.item[length-1-i], self.item[maxIndex] = self.item[maxIndex], self.item[length-1-i]
                

      
                  


if __name__ == "__main__":
    import numpy as np   
    import copy
    
    randomItem = np.random.randint(100, size=10).tolist()
    objItem = copy.deepcopy(randomItem)
    
    s = selectionSort(objItem)
    print("排序前：", s.item)
    # s.sort()
    s.sortOpt()
    print("排序后：", s.item)

    
            
                
            
        
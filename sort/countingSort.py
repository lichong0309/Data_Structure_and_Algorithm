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

# from typing import List
class countingSort(object):
    def __init__(self, item) -> None:
        self.item = item 
        
    def sort(self):
        maxValue = max(self.item)

        # 初始化count为0 
        count = [0 for i in range(maxValue + 1)]
        
        # count计数
        # count[i] 表示self.item中等于i的数量
        for i in self.item:
            count[i] += 1
        
        # count 累计
        # count[i] 表示self.item中小于i和等于i的数量
        for i in range(1, len(count)):
            count[i] += count[i-1]
            
        # 对原始元素排序
        afterSort = [0 for x in range(len(self.item))]    # 初始化aftersort全部元素为0
        for j in range(len(self.item)):
            # 累计count对应的值就是排序的位置
            sortIndex = count[self.item[j]] - 1
            afterSort[sortIndex] = self.item[j]
            count[self.item[j]] -= 1
        
        self.item = afterSort
        

    def sort2(self):
        maxValue = max(self.item)
        
        # count计数
        count = [0 for i in range(maxValue + 1)]
        for i in self.item:
            count[i] += 1
            
        # 对原始元素排序
        afterSort = []
        for i in range(len(count)):
            for j in range(count[i]):
                afterSort.append(i)
        self.item = afterSort
        
    
    

if __name__ == "__main__":
    import numpy as np   
    import copy
    
    # randomItem = np.random.randint(10, size=10).tolist()
    # objItem = copy.deepcopy(randomItem)
    objItem = [6, 7, 2, 8, 6, 6, 2, 8, 1, 4]
    s = countingSort(objItem)
    print("排序前：", s.item)
    s.sort2()
    print("排序后：", s.item)

            



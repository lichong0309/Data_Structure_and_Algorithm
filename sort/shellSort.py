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


class shellSort(object):
    def __init__(self, item) -> None:
        self.item = item
    
    def sort(self):
        # 插入排序是希尔排序中gap=1的特殊情况
        length = len(self.item) 
        gap = length // 2           # 初始化gap
        
        while gap >= 1:
            for i in range(gap, length):
                temp = self.item[i]
                j = i - gap 
                while j >= 0:
                    if self.item[j] > temp:
                        self.item[j+gap] = self.item[j]
                        j = j - gap
                    else:
                        break
                    
                self.item[j+gap] = temp 
                
            gap = gap // 2 
            
            
if __name__ == "__main__":
    import numpy as np   
    import copy
    
    randomItem = np.random.randint(100, size=10).tolist()
    objItem = copy.deepcopy(randomItem)
    
    s = shellSort(objItem)
    print("排序前：", s.item)
    s.sort()
    print("排序后：", s.item)


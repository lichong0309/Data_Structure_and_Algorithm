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

class radixSort(object):
    def __init__(self, item) -> None:
        self.item = item
        
    def sort(self):
        # 得出最大值的位数
        digit = len(str(max(self.item)))
        
        # i： 循环所有的位数, 从最低位开始
        for i in range(digit):
            # 每个位数创建一个0到9的桶：
            bucket = [[] for x in range(10)]
            
            # 对于self.item中的每一个元素
            for j in self.item:
                remain = (j // 10**i) % 10
                bucket[remain].append(j)
            
            # 得到新的元素排列
            self.item = [n for m in bucket for n in m]



if __name__ == "__main__":
    import numpy as np   
    import copy
    
    randomItem = np.random.randint(1000, size=5).tolist()
    objItem = copy.deepcopy(randomItem)
    
    s = radixSort(objItem)
    print("排序前：", s.item)
    s.sort()
    print("排序后：", s.item)

                            
            

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
class bubbleSort(object):
    def __init__(self, item:List[int]) -> None:
        self.item = item
    
    def sort(self):
        # i: 循环的轮次 (从0开始)
        #    因为每次只能冒泡出一个，所以循环次数为len(self.item)
        #    最后一次循环只有一个元素，不需要比较，所以循环次数为len(self.item) - 1
        # j: 每次循环需要比较的次数
        #    每次循环的次数为 总长度len(self.item) -1 - 已经冒泡出的元素i
        #    即：len(self.item) - i - 1
        #    循环比较的索引为：range(0, len(self.item）-i -1)
        for i in range(len(self.item)):             # 循环次数
            for j in range(len(self.item)-i-1):
                if self.item[j] > self.item[j+1]:
                    # 交换
                    temp = self.item[j+1]
                    self.item[j+1] = self.item[j]
                    self.item[j] = temp
                else:
                    pass
                


if __name__ == "__main__":
    import numpy as np   
    import copy
    
    randomItem = np.random.randint(100, size=10).tolist()
    objItem = copy.deepcopy(randomItem)
    
    s = bubbleSort(objItem)
    print("排序前：", s.item)
    s.sort()
    print("排序后：", s.item)

    
                    
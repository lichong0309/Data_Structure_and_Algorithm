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


class mergeSort(object):
    def __init__(self, item) -> None:
        self.item = item 
    
    def merge(self, item):
    
        if len(item) <= 1: 
            return item
        else:
            mid = len(item) // 2
            itemLeft = item[:mid]
            itemRight = item[mid:]
            afterSortLeft = self.merge(itemLeft)
            afterSortRight = self.merge(itemRight)
            
            afterSort = []          # 初始化，接受排序的元素
            
            left_i = 0
            right_i = 0
            
            # 排序，放到afterSort中
            while left_i < len(afterSortLeft) and right_i < len(afterSortRight):
                if afterSortLeft[left_i] <= afterSortRight[right_i]:
                    afterSort.append(afterSortLeft[left_i])
                    left_i += 1
                else:
                    afterSort.append(afterSortRight[right_i])
                    right_i += 1
            
            # left和right最后有一个会有剩余元素，即最大的那几个元素，也要加在afterSort中
            if left_i < len(itemLeft):
                afterSort = afterSort + afterSortLeft[left_i:]
            else:
                afterSort = afterSort + afterSortRight[right_i:]
                                    
            return afterSort
            
            
    def sort(self):
        self.item = self.merge(self.item)
        


if __name__ == "__main__":
    import numpy as np   
    import copy
    
    randomItem = np.random.randint(100, size=5).tolist()
    objItem = copy.deepcopy(randomItem)
    print(objItem)
    # objItem = [2, 86, 33, 88, 22]
    
    s = mergeSort(objItem)
    print("排序前：", s.item)
    s.sort()
    print("排序后：", s.item)

    
        
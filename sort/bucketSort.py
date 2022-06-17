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


class bucketSort(object):
    def __init__(self, item) -> None:
        self.item = item 
        
    def sort(self):
        # 创建bucket
        bucketRange = max(self.item) - min(self.item)
        # 每个桶里面最后3个元素
        bucketNum = int(bucketRange / 3) + 1       # 保证bucket的数量大于一，同时能包含除不尽的数据也能分到最后一个bucket中
        bucketList = [[] for i in range(bucketNum)]     # 创建空桶[[], [], []]
        
        # 将数据元素放到对应的桶中
        for i in range(len(self.item)):
            Nobucket = (self.item[i] - min(self.item)) // 3       # 落入桶的序号
            bucketList[Nobucket].append(self.item[i])       
            
        # 每个bucket进行插入排序
        for li in bucketList:
            # 使用插入排序
            for i in range(1, len(li)):
                temp = li[i]
                j = i - 1
                while j >= 0:
                    if temp < li[j]:
                        li[j+1] = li[j]
                        j = j - 1
                    else:
                        break
                li[j+1] = temp
        
        # 取出bucket中的元素
        afterSort = []
        for li in bucketList:
            for item in li:
                afterSort.append(item)
        
        self.item = afterSort
        

if __name__ == "__main__":
    import numpy as np   
    import copy
    
    randomItem = np.random.randint(100, size=5).tolist()
    objItem = copy.deepcopy(randomItem)
    
    s = bucketSort(objItem)
    print("排序前：", s.item)
    s.sort()
    print("排序后：", s.item)

                        
                






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

class heapSort(object):
    def __init__(self, item) -> None:
        self.item = item
        
    def buildBigHeap(self, pIndex, maxIndex):
        # pIndex: 创建大根堆的父节点
        # maxIndex: (索引)如果父节点的leftIndex和rightIndex 超过了maxIndex，则说明父节点为叶子节点
        leftIndex = pIndex * 2 + 1      # 左孩子节点的索引
        rightIndex = pIndex * 2 + 2     # 右孩子节点的索引
        
        maxNode = pIndex     # 初始化三个节点中最大的节点为pIndex
        
        
        if leftIndex <= maxIndex and self.item[leftIndex] > self.item[pIndex]:
            maxNode = leftIndex
        else:
            pass
        if rightIndex <= maxIndex and self.item[rightIndex] > self.item[pIndex]:
            maxNode = rightIndex
        else:
            pass
            
        if maxNode != pIndex:        # 如果最大的节点不是父节点，则要交换，同时维护孩子节点部分的最大堆的特性
            self.item[pIndex], self.item[maxNode] = self.item[maxNode], self.item[pIndex]
            self.buildBigHeap(maxNode, maxIndex)       # 维护孩子节点的最大堆的特性
        else:
            pass
        
    
    def sort(self):
        length = len(self.item)             
        firstNonLeaf = int((length-1 -1) / 2)         # 第一个非叶子节点的索引
        
        # 初始化的大根堆
        # i: 创建heap的所有父节点的索引，范围为【0，firstNonLeaf】
        #    自下向上创建，所以是【firstNonLeaf, -1, -1】
        for i in range(firstNonLeaf, -1, -1):
            # 为每个父节点创建大根堆
            self.buildBigHeap(i, (length-1))
        
        # 使用初始化的大根堆，对元素进行排序
        # 初始化的大根堆的root节点为所有元素中的最大值
        # root节点和最后一个元素交换位置后，则对于新的root节点来说，需要维持最大堆的特性，所以对于新的root节点需要重新执行buildBigHeap()
        # i: 排序的次数，以为最后剩余一个元素的不需要排序[0, length-1-1]，所以是range(0, length-1)
        for i in range(0, length-1):
            sortIndex = length-1 - i        # 最大堆的root节点的索引，需要和索引为0的元素交换
            self.item[sortIndex], self.item[0] = self.item[0], self.item[sortIndex]
            # 对索引为0的父节点位置最大堆的特性
            self.buildBigHeap(0, sortIndex-1)    # 以为maxIndex是索引，所以sortIndex-1



if __name__ == "__main__":
    import numpy as np   
    import copy
    
    # randomItem = np.random.randint(100, size=5).tolist()
    # objItem = copy.deepcopy(randomItem)
    objItem = [2, 40, 75, 54, 65]
    
    s = heapSort(objItem)
    print("排序前：", s.item)
    s.sort()
    print("排序后：", s.item)
       
            
            
            
            

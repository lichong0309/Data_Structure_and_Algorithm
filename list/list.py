# 创建一个新顺序表
# 判断顺序表是否为空
# 获得顺序表的长度
# 插入————————————
# 将元素插到顺序表的第一个位置
# 将元素插到顺序表的最后一个位置
# 将元素插到顺序表指定的位置
# 删除——————————————
# 删除顺序表的第一个元素
# 删除顺序表的最后一个元素
# 删除顺序表的指定位置的元素
# 查找——————————————
# 查找元素elem在顺序表中的位置，返回索引，如果没有返回-1
# 修改-——————————————
# 修改顺序表中的某一个位置的值


class List(object):
    
    # 创建一个新顺序表
    def __init__(self, elemList) -> None:
        self.elemList = elemList

        
    # 获得顺序表的长度
    def elemListLen(self):
        return len(self.elemList)
    
    # 判断顺序表是否为空   
    def is_empyt(self):
        lennum = self.elemListLen()
        if lennum == 0:
            print("顺序表为空")
        else:
            print("顺序表不为空，长度为：{0}".format(lennum))
            
    # 将元素插到顺序表的第一个位置
    def firstInsert(self, elem):
        self.elemList.insert(0, elem)
        print("将元素插到顺序表的第一个位置")
    
    # 将元素插到顺序表的最后一个位置
    def lastInsert(self, elem):
        self.elemList.append(elem)
        print("将元素插到顺序表的最后一个位置")
    
    # 将元素插到顺序表指定的位置
    def anyInsert(self, elem, i):
        self.elemList.insert(i, elem)
        print("将元素插到顺序表指定的位置")
    
    # 删除顺序表的第一个元素
    def elemDeletFirst(self):
        self.elemList.pop(0)
        print("删除顺序表的第一个元素")
    
    # 删除顺序表的最后一个元素
    def elemeDeletLast(self):
        self.elemList.pop(-1)
        print("删除顺序表的最后一个元素")
    
    # 删除顺序表的指定位置的元素
    def elemDeletAny(self, location):
        self.elemList.pop(location)
        print("删除顺序表的指定位置的元素")
    
    
    # 查找元素elem在顺序表中的位置，返回索引，如果没有返回-1
    def search(self, elem):
        try:
            elemIndex = self.elemList.index(elem)
        except BaseException:
            print("顺序表中没有该元素")
            return -1
        else:
            print("查找成功")
            return elemIndex
            
    # 修改顺序表中的某一个位置的值
    def elemAlter(self, pos, newElem):
        self.elemList[pos] = newElem 
        print("修改顺序表中的某一个位置的值")
        
        
if __name__ == '__main__':
    myList = [1,2,3,4,5,7,8]
    # 创建一个新顺序表
    elemList = List(myList)

    # 判断顺序表是否为空
    elemList.is_empyt()
    # 获得顺序表的长度
    elemLen = elemList.elemListLen()
    # 插入————————————
    # 将元素插到顺序表的第一个位置
    elemList.firstInsert(4)
    # 将元素插到顺序表的最后一个位置
    elemList.lastInsert(3)
    # 将元素插到顺序表指定的位置
    elemList.anyInsert(len(myList) - 1, 10)
    # 删除——————————————
    # 删除顺序表的第一个元素
    elemList.elemDeletFirst()
    # 删除顺序表的最后一个元素
    elemList.elemeDeletLast()
    # 删除顺序表的指定位置的元素
    elemList.elemDeletAny(len(myList) -1)
    # 查找——————————————
    # 查找元素elem在顺序表中的位置，返回索引，如果没有返回-1
    elemindex = elemList.search(0)
    # 修改-——————————————
    # 修改顺序表中的某一个位置的值
    elemList.elemAlter(0,2)
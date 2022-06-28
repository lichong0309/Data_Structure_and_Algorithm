
'''
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        # 队列中存储字典的key
        self.queue = []
        self.length = 0
        self.dict = {}



    def get(self, key: int) -> int:
        if key in self.dict:

            # 1. 退出队列
            self.queue.remove(key)
            # 2. 添加到队列尾部
            self.queue.append(key)
            # 3. 得到value
            value = self.dict[key]

            return value 

        else:
            return -1


    def put(self, key: int, value: int) -> None:
        # 如果key在字典中，则更新
        if key in self.dict:
            
            # 1. 更改value
            self.dict[key] = value 
            # 2. 退出队列
            self.queue.remove(key)
            # 3. 添加到队列尾部
            self.queue.append(key)

            return True

        # 如果key不在字典中，则添加
        else:

            # 如果cache已满，则先逐出一个元素，再添加
            if self.length == self.capacity:
                # 1. 删除队列头部数据：
                discord = self.queue.pop(0)
                # 2. 删除字典中key=discord的元素
                self.dict.pop(discord)
                # 3. 新的key添加到队列尾部
                self.queue.append(key)
                # 4. 新的key添加到字典中
                self.dict[key] = value 
                
                return True

            # 如果cache未满，则直接添加
            else:
                # 1. 添加新的key到字典中
                self.dict[key] = value 
                # 2. 添加新的key到队列尾部
                self.queue.append(key)
                self.length += 1

                return True

        return False

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
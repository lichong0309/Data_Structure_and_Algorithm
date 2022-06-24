from typing import List

import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # dic{key,value}
        # # key: 元素
        # # value: 元素的数量
        # dic = collections.Counter(nums)
        
        # # 按照value排序,从小到大 ->List[tuple(int, int)]
        # dicSort = sorted(dic.items(), key= lambda x:[x[1], x[0]], reverse=True)

        # ans = []
        # count = 1
        # while count <= k:
        #     ans.append(dicSort[count-1][0])
        #     count += 1

        # return ans

        freq = collections.Counter(nums)

        return [f[0] for f in freq.most_common(k)]

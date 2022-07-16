'''
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6



示例 2：
输入：lists = []
输出：[]


示例 3：
输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 类似于归并排序
        # 使用递归

        # 1. 退出条件
        if len(lists) == 1:
            return lists[0]

        if len(lists) == 0:
            return None
            
        else:
            # 2. 拆分
            # 2.1 找到中间位置
            mid = int(len(lists)/2)
            left = lists[:mid]  
            right = lists[mid:]

            # 2.2 迭代
            leftHead = self.mergeKLists(left)
            rightHead = self.mergeKLists(right)

            # 3. 排序
            newNode = ListNode(val=-1,next=None)
            cur = newNode
            while leftHead != None and rightHead != None:
                if leftHead.val <= rightHead.val:
                    cur.next = leftHead
                    leftHead = leftHead.next
                    cur = cur.next      # cur指向最后一个节点
                else:
                    cur.next = rightHead
                    rightHead = rightHead.next
                    cur = cur.next      # cur指向最后一个节点
    
            # 4. 合并
            if leftHead != None:
                cur.next = leftHead 
            if rightHead != None:
                cur.next = rightHead

            return newNode.next
            
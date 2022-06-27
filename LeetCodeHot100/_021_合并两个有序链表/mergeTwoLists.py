'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

### 参考leetCodeHot100 第148题

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建新的链表存放最终的结果
        newHead = ListNode(val=0, next=None)

        cur = newHead
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                # 创建新节点
                newNode = ListNode(val=list1.val, next=None)
                cur.next = newNode  # 添加新节点到newHead链表中
                cur = cur.next      # cur永远指向newHead链表的最后一个节点
                list1 = list1.next
            else:
                # 创建新节点：
                newNode = ListNode(val=list2.val, next=None)
                cur.next = newNode  # 添加新节点到newHead链表中
                cur = cur.next      # cur永远指向newHead链表的最后一个节点
                list2 = list2.next
        
        if list1 != None:
            cur.next = list1
        if list2 != None:
            cur.next = list2
        
        return newHead.next

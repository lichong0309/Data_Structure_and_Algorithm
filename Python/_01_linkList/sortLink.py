from singleLink import singleLink, singleLinkNode
from typing import Optional

# LeetCode 148 排序链表



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next
class Solution:
    def sortList(self, head: Optional[singleLinkNode]) -> Optional[singleLinkNode]:
        # cur_i = head
        # while cur_i.next != None:
        #     cur_j = head 
        #     while cur_j.next != None:
        #         if cur_j.data > cur_j.next.data:
        #             cur_j.data, cur_j.next.data = cur_j.next.data, cur_j.data
        #         else:
        #             pass
        #         cur_j = cur_j.next
        #     cur_i = cur_i.next
        
        # cur = head
        # ans = []
        # while cur != None:
        #     ans.append(cur.data)
        # return ans

        # 1. 迭代退出条件
        if head == None or head.next == None:
            return head
        
        else:
            # 2. 拆分
            # 2.1 找到中间位置
                # 1) 一个指针走一次一步slow
                # 2) 一个指针走一次两步fast
                # 3) 一个指针记录中间位置pre
            slow, fast, pre = head, head, head
            while fast != None and fast.next != None:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            
            pre.next = None
            # pre为左链表的尾节点(pre.next=None)，slow为右链表的头节点
            # 2.2 迭代
            leftHead = self.sortList(head)
            rightHead = self.sortList(slow)

            # 排序
            tempHead = singleLinkNode(0)           # 创建一个新链表存放排序好的链表
            cur = tempHead
            while leftHead != None and rightHead != None:
                if leftHead.data > rightHead.data:
                    # 添加节点到tempHead链表中
                    newNode = singleLinkNode(leftHead.data)        # 按照leftHead.data创建新的节点
                    cur.next = newNode
                    cur = cur.next          # cur永远指向最后一个节点
                    leftHead = leftHead.next
                else:
                    newNode = singleLinkNode(rightHead.data)       # 按照rightHead.data创建新的节点
                    cur.next = newNode
                    cur = cur.next           # cur永远指向最后一个节点
                    rightHead = rightHead.next

            # 合并
            # 添加leftHead链表或rightHead链表中剩余的节点到tempHead
            if leftHead != None:
                cur.next = leftHead
            if rightHead != None:
                cur.next = rightHead

            return tempHead.next            # 第一个节点是初始化tempHead创建的，应该从第二个开始返回
        
        
a = [4,2,1,3]
link = singleLink()
for i in a:
    link.appendInTail(singleLinkNode(i))
item = link.items()

cl = Solution()
cl.sortList(link.head)
item = link.items()

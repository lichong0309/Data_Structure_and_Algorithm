'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 联系leetCodeHot 100 第21题

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 冒泡排序，超时
        # # cur_i = head
        # # while cur_i.next != None:
        # #     cur_j = head 
        # #     while cur_j.next != None:
        # #         if cur_j.val > cur_j.next.val:
        # #             cur_j.val, cur_j.next.val = cur_j.next.val, cur_j.val
        # #         else:
        # #             pass
        # #         cur_j = cur_j.next
        # #     cur_i = cur_i.next
        
        # # cur = head
        # # ans = []
        # # while cur != None:
        # #     ans.append(cur.val)
        # # return ans


        # # 第一种解决方法， 执行时间1180ms
        # # 使用归并排序
        
        # # 1. 迭代退出条件
        # if head == None or head.next == None:
        #     return head
        
        # else:
        #     # 2. 拆分
        #     # 2.1 找到中间位置
        #         # 1) 一个指针走一次一步slow
        #         # 2) 一个指针走一次两步fast
        #         # 3) 一个指针记录中间位置pre
        #     slow, fast, pre = head, head, head
        #     while fast != None and fast.next != None:
        #         pre = slow
        #         slow = slow.next
        #         fast = fast.next.next
            
        #     pre.next = None           # 将链表分成两部分
        
        #     # pre为左链表的尾节点(pre.next=None)，slow为右链表的头节点
        #     # 2.2 迭代
        #     leftHead = self.sortList(head)
        #     rightHead = self.sortList(slow)

        #     # 排序
        #     tempHead = ListNode(val=0, next=None)           # 创建一个新链表存放排序好的链表
        #     cur = tempHead
        #     while leftHead != None and rightHead != None:
        #         if leftHead.val <= rightHead.val:
        #             # 添加节点到tempHead链表中
        #             newNode = ListNode(leftHead.val)        # 按照leftHead.val创建新的节点
        #             cur.next = newNode
        #             cur = cur.next          # cur永远指向最后一个节点
        #             leftHead = leftHead.next
        #         else:
        #             newNode = ListNode(rightHead.val)       # 按照rightHead.val创建新的节点
        #             cur.next = newNode
        #             cur = cur.next           # cur永远指向最后一个节点
        #             rightHead = rightHead.next

        #     # 合并
        #     # 添加leftHead链表或rightHead链表中剩余的节点到tempHead
        #     if leftHead != None:
        #         cur.next = leftHead
        #     if rightHead != None:
        #         cur.next = rightHead

        #     return tempHead.next            # 第一个节点是初始化tempHead创建的，应该从第二个开始返回


        # 第二种解决方法 执行时间 224ms
        # 使用list存放链表中的数据，对list进行排序，将list的元素赋值给链表中的每个节点
        nodes_list = []
        cur = head
        while cur != None:
            nodes_list.append(cur.val)
            cur = cur.next

        # 对node_list进行排序
        nodes_list.sort()

        cur = head
        ind = 0
        while cur != None:
            cur.val = nodes_list[ind]
            cur = cur.next
            ind = ind + 1
        
        return head
            
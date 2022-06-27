

'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 
示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''




from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 得到 l1 链表中node的值，存放到list1中
        cur = l1
        list1 = []
        while cur != None:
            list1.append(cur.val)
            cur = cur.next
        # 得到 l2 链表中node的值，存放到list2中
        cur = l2 
        list2 = []
        while cur != None:
            list2.append(cur.val)
            cur = cur.next
        
        # 将 l1 链表转化为整数
        count1 = 0
        for i in range(len(list1)):
            val = list1[i]
            count1 = count1 + val * (10**i)

        # 将 l2 链表转化为整数
        count2 = 0 
        for i in range(len(list2)):
            val = list2[i]
            count2 = count2 + val * (10**i) 
        
        # 计算最终结果
        count = count1 + count2
        # 将count从 int-> str(可迭代)
        strcount = str(count)

        # 将结果存放到新的链表中
        newHead = ListNode(val=0, next=None)        # 创建新的链表
        cur = newHead
        # 从后往前遍历strcount，并将每个值存放到一个新的节点中
        for i in range(len(strcount)-1, -1, -1):
            val = int(strcount[i])          # 得到节点的值
            newNode = ListNode(val=int(val), next=None) # 创建新的节点  
            cur.next = newNode              # 新的节点加入链表newHead中    
            cur = cur.next                  # cur指向新的节点
        
        return newHead.next

            
            


        
'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

 

示例 1：
输入：head = [1,2,2,1]
输出：true


示例 2：
输入：head = [1,2]
输出：false
 

提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9
 

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # # 第一种方法，将链表转换成list， 执行时间：736ms
        # linkList = []

        # cur = head 
        # while cur != None:
        #     linkList.append(cur.val)
        #     cur = cur.next 

        # tempList = list(reversed(linkList))

        # if tempList == linkList:
        #     return True
        # else:
        #     return False
        
        
        # 第二种方法：反转前半部分链表和后半部分进行对比, 执行时间：564ms
        # 1. 找到中间Node
        #   1.1 设计三个指针
        #     1) pre: 记录中间位置和前一个节点的位置（反转链表）
        #     2) slow: 一次移动一个步长
        #     3) fast: 一次移动两个步长 
        # 2. 反转链表前部的节点
        pre, slow, fast = None, head, head 
        
        # 循环条件说明：
        # 1. fast不能为None，如果fast为None，则不存在fast.next, 会报错
        # 2. fast.next不能为None，如果fast.next为None，则不存在fast.next.next，会报错
        # 综上 循环条件为： fast != None and fast.next != None 
        
        while fast != None and fast.next != None:
            fast = fast.next.next    # fast指针移动步长
            # 反转链表：
            next = slow.next         # 拉住链表后面的节点
            slow.next = pre          # 反转链表
            # 移动指针，反转下面的节点
            pre = slow               # 移动pre指针
            slow = next              # 移动slow指针

        # 节点为单数
        if fast != None:
            leftHead = pre
            rightHead = slow.next

        # 节点为双数
        if fast == None:
            leftHead = pre
            rightHead = slow
        
        # 遍历左右指针节点，进行对比
        while leftHead != None and rightHead != None:
            if leftHead.val != rightHead.val:
                return False
            else:
                leftHead = leftHead.next 
                rightHead = rightHead.next 

        return True


    
        

        
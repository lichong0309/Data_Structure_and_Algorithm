
'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # # 方法一：使用list存放链表中node的值，对list进行操作
        
        
        # # 存放链表中Node的值
        # linkList = []
        
        # # 将node的值存放到linkList中
        # cur = head 
        # while cur != None:
        #     linkList.append(cur.val)
        #     cur = cur.next
        
        # # 反转linkList
        # linkList.reverse()

        # # 重新赋值链表中Node的val
        # cur = head
        # i = 0
        # while cur != None:
        #     cur.val = linkList[i]
        #     cur = cur.next 
        #     i = i + 1 
        
        # return head 
            
            
            
        # 方法二：对链表直接操作，指针指向进行翻转
        cur = head 
        pre = None 
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur 
            cur = next 
            
        return pre 

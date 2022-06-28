
'''

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]


示例 2：
输入：head = [1], n = 1
输出：[]


示例 3：
输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

进阶：你能尝试使用一趟扫描实现吗？

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # # 第一种方法：链表转list, 超时
        
        # # 转化成list
        # cur = head
        # linkList = [] 
        # while cur != None:
        #     linkList.append(cur.val)
        # # 删除倒数第n个节点
        # linkList.pop(-n)

        # # 重新分配val给节点
        # cur = head 
        # pre = None          # 记录删除节点后最后一个节点的位置
        # while linkList != []:
        #     cur.val = linkList[0]
        #     linkList.pop(0)
        #     pre = cur
        #     cur = cur.next 
        # # 最后一个节点指向None
        # pre.next = None
        # return head 


        # 第二种方法：直接遍历链表
        # 添加虚拟头结点
        headNode = ListNode(val=0,next=head)
        head = headNode
        
        # 设置快慢指针
        fast = head 
        low = head 

        for i in range(n):
            fast = fast.next

         # 循环结束后, fast指向最后一个节点，low指向要删除的节点的 上一个节点
        while fast.next != None:
            low = low.next
            fast = fast.next

        # 删除节点
        low.next = low.next.next

        return head.next

        


        
            
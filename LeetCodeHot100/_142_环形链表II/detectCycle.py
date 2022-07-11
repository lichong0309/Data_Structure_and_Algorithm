'''
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

 

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。



示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。



示例 3:
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 

提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
 

进阶：你是否可以使用 O(1) 空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''



# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        # # hash法，链表转化为list
        # cur = head 
        # linkList = []   
        # while cur != None:
        #     # 存在环状
        #     if cur in linkList:
        #         return cur
        #     else:
        #         linkList.append(cur)
        #         cur = cur.next
        # return None


        # 遍历链表

        # 1. low指针在环形处最多走了一整圈
        #       证明：因为fast比low早进入或者同时进入环形处，所以fast追上low的最长距离不超过环形处的节点的数量，
        #            又因为low每次只走一个节点，所以当相遇时，low指针在环形处最多走了一整圈，或者小于一整圈
        # 2. 设head节点到环形处的第一个节点的节点的数量为 x
        #    设环形处第一个节点到fast和low相遇处的节点的节点数量为 y，
        #    设fast和low相遇处的节点到环形处的第一个节点的节点数量为 z
        #    存在关系： z+y = k (k为环形处一整圈的节点的数量) 
        #             low节点走的距离： x+y
        #             fast节点走的距离为： x + y + n(y+z)
        #             又有： (x+y)/1 = (x+y+n(y+z))/2       
        #             ==> x = nk-y = z+(n-1)k
        # 综上：说明当fast和low相遇时，low指针从相遇节点出发，行走z个节点和(n-1)k个节点，
        #      会遇到一个同时且同步从head节点出发的指针，并且他们会在环形处的第一个节点处遇到

        # 判断是否存在环形链表
        fast, low = head, head 

        flag = 0
        while fast and fast.next:
            fast = fast.next.next
            low = low.next

            if fast is low:
                flag = 1
                break           # 退出循环
            else:
                pass
        
        # 找到pos位置
        if flag == 1:
            start = head 

            while start is not fast:
                start = start.next 
                fast = fast.next

            return start
        else:
            return None

            
    
        

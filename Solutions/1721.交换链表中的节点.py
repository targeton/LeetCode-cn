#
# @lc app=leetcode.cn id=1721 lang=python3
#
# [1721] 交换链表中的节点
#
# https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list/description/
#
# algorithms
# Medium (65.15%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 12.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你链表的头节点 head 和一个整数 k 。
# 
# 交换 链表正数第 k 个节点和倒数第 k 个节点的值后，返回链表的头节点（链表 从 1 开始索引）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[1,4,3,2,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [7,9,6,6,7,8,3,0,9,5], k = 5
# 输出：[7,9,6,6,8,7,3,0,9,5]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1], k = 1
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：head = [1,2], k = 1
# 输出：[2,1]
# 
# 
# 示例 5：
# 
# 
# 输入：head = [1,2,3], k = 2
# 输出：[1,2,3]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目是 n
# 1 
# 0 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1, head)
        n = dummy
        while k:
            n = n.next
            k -= 1
        n1 = n
        while n.next:
            head = head.next
            n = n.next
        n1.val, head.val = head.val, n1.val
        return dummy.next
# @lc code=end


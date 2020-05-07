#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (64.38%)
# Likes:    524
# Dislikes: 0
# Total Accepted:    58.5K
# Total Submissions: 89.7K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 
# 示例 1:
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2:
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def quickSort(start, end):
            if start == end:
                return
            tmp = start.val
            p, q = start, start.next
            while q != end:
                if q.val < tmp:
                    p.val = q.val
                    p = p.next
                    q.val = p.val
                q = q.next
            p.val = tmp
            quickSort(start, p)
            quickSort(p.next, end)
        
        quickSort(head, None)
        return head

        
# @lc code=end


#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.45%)
# Likes:    575
# Dislikes: 0
# Total Accepted:    96.7K
# Total Submissions: 193.7K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy, N = ListNode(-1), len(lists)
        cur = dummy
        tmp = [lists[i] for i in range(N)]
        while True:
            index, mi = -1, float('inf')
            for i in range(N):
                if not tmp[i]:
                    continue
                if tmp[i].val < mi:
                    index, mi = i, tmp[i].val
            if index < 0:
                break
            cur.next, tmp[index] = tmp[index], tmp[index].next
            cur = cur.next
        return dummy.next

# @lc code=end


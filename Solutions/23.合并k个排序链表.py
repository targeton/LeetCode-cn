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
        pq = []
        for i,n in enumerate(lists):
            if not n:
                continue
            heapq.heappush(pq,(n.val, i))
        dummy = ListNode(-1)
        cur = dummy
        while len(pq) > 0:
            _, i = heapq.heappop(pq)
            cur.next, lists[i] = lists[i], lists[i].next
            cur = cur.next
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
        return dummy.next

# @lc code=end


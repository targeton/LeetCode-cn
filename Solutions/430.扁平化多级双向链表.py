#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#
# https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/description/
#
# algorithms
# Medium (53.96%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 61.2K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]'
#
# 
# 多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
# 
# 给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# 输出：[1,2,3,7,8,11,12,9,10,4,5,6]
# 解释：
# 
# 输入的多级列表如下图所示：
# 
# 
# 
# 扁平化后的链表如下图：
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2,null,3]
# 输出：[1,3,2]
# 解释：
# 
# 输入的多级列表如下图所示：
# 
# ⁠ 1---2---NULL
# ⁠ |
# ⁠ 3---NULL
# 
# 
# 示例 3：
# 
# 输入：head = []
# 输出：[]
# 
# 
# 
# 
# 如何表示测试用例中的多级链表？
# 
# 以 示例 1 为例：
# 
# ⁠1---2---3---4---5---6--NULL
# ⁠        |
# ⁠        7---8---9---10--NULL
# ⁠            |
# ⁠            11--12--NULL
# 
# 序列化其中的每一级之后：
# 
# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
# 
# 
# 为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。
# 
# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
# 
# 
# 合并所有序列化结果，并去除末尾的 null 。
# 
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# 
# 
# 
# 提示：
# 
# 
# 节点数目不超过 1000
# 1 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # head为空，或者既没有子节点也没有后继节点
        if not head or (not head.child and not head.next):
            return head
        # 使用递归操作，分别处理后继节点和子节点
        nextHead = self.flatten(head.next)
        childHead = self.flatten(head.child)
        # 如果子节点的扁平操作返回非空值则将返回节点接入到当前节点后继节点；为空值则不需要进行任何操作（当前就是扁平状态）
        if childHead:
            head.next, childHead.prev, head.child = childHead, head, None
            # 如果后继节点的扁平操作返回值非空值，则需要遍历找到返回的扁平子节点双向链表的尾节点，与后继节点再进行拼接；为空指则不需要进行任何操作
            if nextHead:
                while childHead and childHead.next:
                    childHead = childHead.next
                childHead.next, nextHead.prev = nextHead, childHead
        return head
        
# @lc code=end


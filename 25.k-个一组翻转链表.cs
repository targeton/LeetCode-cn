/*
 * @lc app=leetcode.cn id=25 lang=csharp
 *
 * [25] K 个一组翻转链表
 *
 * https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
 *
 * algorithms
 * Hard (54.56%)
 * Likes:    405
 * Dislikes: 0
 * Total Accepted:    42.6K
 * Total Submissions: 74.9K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
 * 
 * k 是一个正整数，它的值小于或等于链表的长度。
 * 
 * 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
 * 
 * 
 * 
 * 示例：
 * 
 * 给你这个链表：1->2->3->4->5
 * 
 * 当 k = 2 时，应当返回: 2->1->4->3->5
 * 
 * 当 k = 3 时，应当返回: 3->2->1->4->5
 * 
 * 
 * 
 * 说明：
 * 
 * 
 * 你的算法只能使用常数的额外空间。
 * 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode ReverseKGroup(ListNode head, int k) {
        return ReverseKGroup(head, k, 1);
    }

    private ListNode ReverseKGroup(ListNode head, int k, int index) {
        if(head == null) {
            return head;
        }
        if(index == k) {
            head.next = ReverseKGroup(head.next, k, 1);
            return head;
        }
        var find = ReverseKGroup(head.next, k, index + 1);
        if(find != null){
            var tmp = head.next;
            head.next = tmp.next;
            tmp.next = head;
            return find;
        } else {
            if (index == 1)
                return head;
            else 
                return null;
        }
    }

}
// @lc code=end


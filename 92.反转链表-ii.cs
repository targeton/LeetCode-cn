/*
 * @lc app=leetcode.cn id=92 lang=csharp
 *
 * [92] 反转链表 II
 *
 * https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
 *
 * algorithms
 * Medium (46.82%)
 * Likes:    315
 * Dislikes: 0
 * Total Accepted:    38.7K
 * Total Submissions: 78.3K
 * Testcase Example:  '[1,2,3,4,5]\n2\n4'
 *
 * 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
 * 
 * 说明:
 * 1 ≤ m ≤ n ≤ 链表长度。
 * 
 * 示例:
 * 
 * 输入: 1->2->3->4->5->NULL, m = 2, n = 4
 * 输出: 1->4->3->2->5->NULL
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
    public ListNode ReverseBetween(ListNode head, int m, int n) {
        ListNode prev = null;
        ListNode mPos = null;
        ListNode result = head;
        int index = 0;
        while(index < n){
            index++;
            if(index < m){
                prev = head;
                head = head.next;
                continue;
            }
            if(index == m){
                mPos = head;
            }
            var tmp = head.next;
            head.next = prev;
            prev = head;
            head = tmp;
        }
        if(mPos.next != null){
            mPos.next.next = prev;
        }
        mPos.next = head;
        if(m == 1)
            result = prev;
        return result;
    }
}
// @lc code=end


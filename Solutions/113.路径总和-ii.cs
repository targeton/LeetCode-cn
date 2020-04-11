/*
 * @lc app=leetcode.cn id=113 lang=csharp
 *
 * [113] 路径总和 II
 *
 * https://leetcode-cn.com/problems/path-sum-ii/description/
 *
 * algorithms
 * Medium (57.05%)
 * Likes:    127
 * Dislikes: 0
 * Total Accepted:    16.4K
 * Total Submissions: 28.7K
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
 *
 * 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
 * 
 * 说明: 叶子节点是指没有子节点的节点。
 * 
 * 示例:
 * 给定如下二叉树，以及目标和 sum = 22，
 * 
 * ⁠             5
 * ⁠            / \
 * ⁠           4   8
 * ⁠          /   / \
 * ⁠         11  13  4
 * ⁠        /  \    / \
 * ⁠       7    2  5   1
 * 
 * 
 * 返回:
 * 
 * [
 * ⁠  [5,4,11,2],
 * ⁠  [5,8,4,5]
 * ]
 * 
 * 
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public IList<IList<int>> PathSum(TreeNode root, int sum) {
        var result = new List<IList<int>>();
        if(root == null)
            return result;
        if(root.left == null && root.right == null && root.val == sum){
            result.Add(new List<int>(){root.val});
            return result;
        }
        var left = root.left == null ? null : PathSum(root.left, sum-root.val);
        if(left != null){
            foreach(var l in left){
                l.Insert(0, root.val);
                result.Add(l);
            }
        }    
        var right = root.right == null ? null : PathSum(root.right, sum-root.val);
        if(right != null){
            foreach(var r in right){
                r.Insert(0, root.val);
                result.Add(r);
            }
        }
        return result;
    }
}


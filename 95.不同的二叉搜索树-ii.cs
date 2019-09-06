/*
 * @lc app=leetcode.cn id=95 lang=csharp
 *
 * [95] 不同的二叉搜索树 II
 *
 * https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
 *
 * algorithms
 * Medium (58.29%)
 * Likes:    182
 * Dislikes: 0
 * Total Accepted:    10.4K
 * Total Submissions: 17.6K
 * Testcase Example:  '3'
 *
 * 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
 * 
 * 示例:
 * 
 * 输入: 3
 * 输出:
 * [
 * [1,null,3,2],
 * [3,2,null,1],
 * [3,1,null,null,2],
 * [2,1,3],
 * [1,null,2,null,3]
 * ]
 * 解释:
 * 以上的输出对应以下 5 种不同结构的二叉搜索树：
 * 
 * ⁠  1         3     3      2      1
 * ⁠   \       /     /      / \      \
 * ⁠    3     2     1      1   3      2
 * ⁠   /     /       \                 \
 * ⁠  2     1         2                 3
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
    public IList<TreeNode> GenerateTrees(int n) {
        if(n==0)
            return new List<TreeNode>();
        return GenerateSubTree(1,n);
    }

    private IList<TreeNode> GenerateSubTree(int s, int e){
        var result = new List<TreeNode>();
        for(int i=s; i<=e; i++){
            var left = GenerateSubTree(s,i-1);
            var right = GenerateSubTree(i+1,e);
            for(int m=0; m<left.Count; m++){
                for(int n=0; n<right.Count; n++){
                    var root = new TreeNode(i);
                    root.left = left[m];
                    root.right = right[n];
                    result.Add(root);
                }
            }
        }
        return result.Count == 0 ? new List<TreeNode>(){null} : result;
    }
}


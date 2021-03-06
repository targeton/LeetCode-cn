/*
 * @lc app=leetcode.cn id=96 lang=csharp
 *
 * [96] 不同的二叉搜索树
 *
 * https://leetcode-cn.com/problems/unique-binary-search-trees/description/
 *
 * algorithms
 * Medium (61.58%)
 * Likes:    242
 * Dislikes: 0
 * Total Accepted:    15.3K
 * Total Submissions: 24.6K
 * Testcase Example:  '3'
 *
 * 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
 * 
 * 示例:
 * 
 * 输入: 3
 * 输出: 5
 * 解释:
 * 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
 * 
 * ⁠  1         3     3      2      1
 * ⁠   \       /     /      / \      \
 * ⁠    3     2     1      1   3      2
 * ⁠   /     /       \                 \
 * ⁠  2     1         2                 3
 * 
 */
public class Solution {
    public int NumTrees(int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        for(int i=1; i<=n; i++){
            // accumulate kinds when j as root. (1,...,j-1 are in left subtree and j+1,...,n are in right subtree, when j as root.)
            for(int j=1; j<=i; j++){
                dp[i] += dp[i-j]*dp[j-1];
            }            
        }
        return dp[n];
    }
}


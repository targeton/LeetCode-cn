/*
 * @lc app=leetcode.cn id=72 lang=csharp
 *
 * [72] 编辑距离
 *
 * https://leetcode-cn.com/problems/edit-distance/description/
 *
 * algorithms
 * Hard (54.68%)
 * Likes:    355
 * Dislikes: 0
 * Total Accepted:    15.4K
 * Total Submissions: 28.2K
 * Testcase Example:  '"horse"\n"ros"'
 *
 * 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
 * 
 * 你可以对一个单词进行如下三种操作：
 * 
 * 
 * 插入一个字符
 * 删除一个字符
 * 替换一个字符
 * 
 * 
 * 示例 1:
 * 
 * 输入: word1 = "horse", word2 = "ros"
 * 输出: 3
 * 解释: 
 * horse -> rorse (将 'h' 替换为 'r')
 * rorse -> rose (删除 'r')
 * rose -> ros (删除 'e')
 * 
 * 
 * 示例 2:
 * 
 * 输入: word1 = "intention", word2 = "execution"
 * 输出: 5
 * 解释: 
 * intention -> inention (删除 't')
 * inention -> enention (将 'i' 替换为 'e')
 * enention -> exention (将 'n' 替换为 'x')
 * exention -> exection (将 'n' 替换为 'c')
 * exection -> execution (插入 'u')
 * 
 * 
 */
public class Solution {
    public int MinDistance(string word1, string word2) {
        int m = word1.Length;
        int n = word2.Length;
        int[,] dp = new int[m+1,n+1];
        for(int i=0; i<m+1; i++){
            for(int j=0; j<n+1; j++){
                if(i == 0 || j == 0){
                    dp[i,j] = Math.Max(i,j);
                    continue;
                }
                if(word1[i-1] == word2[j-1])
                    dp[i,j] = dp[i-1,j-1];
                else{
                    var tmp = Math.Min(dp[i-1,j-1], dp[i,j-1]);
                    dp[i,j] = Math.Min(tmp, dp[i-1, j]) + 1;
                }
            }
        }
        return dp[m,n];
    }
}


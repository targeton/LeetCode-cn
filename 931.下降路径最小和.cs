/*
 * @lc app=leetcode.cn id=931 lang=csharp
 *
 * [931] 下降路径最小和
 *
 * https://leetcode-cn.com/problems/minimum-falling-path-sum/description/
 *
 * algorithms
 * Medium (55.75%)
 * Likes:    19
 * Dislikes: 0
 * Total Accepted:    2.4K
 * Total Submissions: 4.1K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。
 * 
 * 下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：[[1,2,3],[4,5,6],[7,8,9]]
 * 输出：12
 * 解释：
 * 可能的下降路径有：
 * 
 * 
 * 
 * [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
 * [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
 * [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
 * 
 * 
 * 和最小的下降路径是 [1,4,7]，所以答案是 12。
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= A.length == A[0].length <= 100
 * -100 <= A[i][j] <= 100
 * 
 * 
 */
public class Solution {
    public int MinFallingPathSum(int[][] A) {
        int n = A.Length;
        int[] dp = new int[n+2];
        dp[0] = int.MaxValue;
        dp[n+1] = int.MaxValue;
        for(int i=0; i<n; i++){
            dp[i+1] = A[0][i];
        }
        for(int i=1; i<n; i++){
            int[] array = new int[n+2];
            array[0] = dp[0];
            array[n+1] = dp[n+1];
            for(int j=0; j<n; j++){
                var tmp = new List<int>(){dp[j], dp[j+1], dp[j+2]};
                array[j+1] = tmp.Min() + A[i][j];
            }
            dp = array;
        }
        return dp.Skip(1).Take(n).Min();
    }
}


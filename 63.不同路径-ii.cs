/*
 * @lc app=leetcode.cn id=63 lang=csharp
 *
 * [63] 不同路径 II
 *
 * https://leetcode-cn.com/problems/unique-paths-ii/description/
 *
 * algorithms
 * Medium (31.69%)
 * Likes:    153
 * Dislikes: 0
 * Total Accepted:    20.2K
 * Total Submissions: 63.6K
 * Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
 *
 * 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
 * 
 * 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
 * 
 * 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
 * 
 * 
 * 
 * 网格中的障碍物和空位置分别用 1 和 0 来表示。
 * 
 * 说明：m 和 n 的值均不超过 100。
 * 
 * 示例 1:
 * 
 * 输入:
 * [
 * [0,0,0],
 * [0,1,0],
 * [0,0,0]
 * ]
 * 输出: 2
 * 解释:
 * 3x3 网格的正中间有一个障碍物。
 * 从左上角到右下角一共有 2 条不同的路径：
 * 1. 向右 -> 向右 -> 向下 -> 向下
 * 2. 向下 -> 向下 -> 向右 -> 向右
 * 
 * 
 */
public class Solution {
    public int UniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.Length;
        if(m == 0) return 0;
        int n = obstacleGrid[0].Length;
        int[,] dp = new int[m,n];
        if(obstacleGrid[0][0] == 1) return 0;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if(i==0 && j==0){
                    dp[i,j] = 1;
                }else if(i==0){
                    dp[i,j] = obstacleGrid[i][j] == 1 ? 0 : dp[i,j-1];
                }else if(j==0){
                    dp[i,j] = obstacleGrid[i][j] == 1 ? 0 : dp[i-1,j];
                }else{
                    dp[i,j] = obstacleGrid[i][j] == 1 ? 0 : dp[i,j-1] + dp[i-1,j];
                }                
            }
        }
        return dp[m-1,n-1];
    }
}


/*
 * @lc app=leetcode.cn id=200 lang=csharp
 *
 * [200] 岛屿数量
 *
 * https://leetcode-cn.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (45.35%)
 * Likes:    415
 * Dislikes: 0
 * Total Accepted:    66.4K
 * Total Submissions: 139.7K
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * 给定一个由 '1'（陆地）和
 * '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
 * 
 * 示例 1:
 * 
 * 输入:
 * 11110
 * 11010
 * 11000
 * 00000
 * 
 * 输出: 1
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * 11000
 * 11000
 * 00100
 * 00011
 * 
 * 输出: 3
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int NumIslands(char[][] grid) {
        if(grid == null || grid.Length == 0)
            return 0;
        int[] xDelta = new int[]{-1,0,1,0};
        int[] yDelta = new int[]{0,-1,0,1};
        int result = 0;
        var queue = new Queue<int[]>();
        int xL = grid.Length, yL = grid[0].Length;
        // 遍历二维网格，如果当前位置为陆地，则通过宽度优先搜索，搜索该位置横纵方向是否有相邻陆地，取队列头元素时将该位置的陆地置0，防止重复计数
        for(int i = 0; i < xL; i++){
            for(int j = 0; j < yL; j++){
                if(grid[i][j] == '0')
                    continue;
                grid[i][j] = '0';
                result++;
                queue.Enqueue(new int[]{i,j});
                while(queue.Count() > 0){
                    int[] item = queue.Dequeue();
                    for(int k = 0; k < 4; k++){
                        int ii = item[0] + xDelta[k];
                        int jj = item[1] + yDelta[k];
                        if(ii < 0 || ii >= xL || jj < 0 || jj >= yL)
                            continue;
                        if(grid[ii][jj] == '1'){
                            queue.Enqueue(new int[]{ii, jj});
                            grid[ii][jj] = '0';
                        }
                    }
                }
            }
        }
        return result;
    }
}
// @lc code=end


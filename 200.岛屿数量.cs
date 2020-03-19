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
public class Solution
{
    // 并查集
    class UnionFind
    {
        private int _count;
        private int[] _roots;
        private int[] _ranks;

        public UnionFind(char[][] grid)
        {
            _count = 0;
            int m = grid.Length, n = grid[0].Length;
            _roots = new int[m * n];
            _ranks = new int[m * n];
            for (int i = 0; i < m; ++i)
            {
                for (int j = 0; j < n; ++j)
                {
                    if (grid[i][j] == '1')
                    {
                        ++_count;
                        _roots[i * n + j] = i * n + j;
                    }
                    _ranks[i * n + j] = 0;
                }
            }
        }

        public int Find(int i)
        {
            // while (_roots[i] != i)
            // {
            //     i = _roots[i];
            // }
            // return i;
            if (_roots[i] != i)
                _roots[i] = Find(_roots[i]);
            return _roots[i];
        }

        public void Union(int x, int y)
        {
            int rootX = Find(x);
            int rootY = Find(y);
            if (rootX != rootY)
            {
                if (_ranks[rootX] < _ranks[rootY])
                {
                    _roots[rootX] = rootY;
                }
                else if (_ranks[rootX] > _ranks[rootY])
                {
                    _roots[rootY] = rootX;
                }
                else
                {
                    _roots[rootY] = rootX;
                    _ranks[rootX] += 1;
                }
                --_count;
            }
        }

        public int Count() { return _count; }
    }

    public int NumIslands(char[][] grid)
    {
        if (grid == null || grid.Length == 0 || grid[0].Length == 0)
            return 0;
        int xL = grid.Length, yL = grid[0].Length;
        var uf = new UnionFind(grid);
        for (int i = 0; i < xL; i++)
        {
            for (int j = 0; j < yL; j++)
            {
                if (grid[i][j] == '1') {
                    grid[i][j] = '0';
                    if (i - 1 >= 0 && grid[i - 1][j] == '1')
                        uf.Union(i * yL + j, (i - 1) * yL + j);
                    if (i + 1 < xL && grid[i + 1][j] == '1')
                        uf.Union(i * yL + j, (i + 1) * yL + j);
                    if (j - 1 >= 0 && grid[i][j - 1] == '1')
                        uf.Union(i * yL + j, i * yL + j - 1);
                    if (j + 1 < yL && grid[i][j + 1] == '1')
                        uf.Union(i * yL + j, i * yL + j + 1);
                }
            }
        }
        return uf.Count();
    }
}
// @lc code=end


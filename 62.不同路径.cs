/*
 * @lc app=leetcode.cn id=62 lang=csharp
 *
 * [62] 不同路径
 *
 * https://leetcode-cn.com/problems/unique-paths/description/
 *
 * algorithms
 * Medium (55.27%)
 * Likes:    313
 * Dislikes: 0
 * Total Accepted:    36.4K
 * Total Submissions: 65.1K
 * Testcase Example:  '3\n2'
 *
 * 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
 * 
 * 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
 * 
 * 问总共有多少条不同的路径？
 * 
 * 
 * 
 * 例如，上图是一个7 x 3 的网格。有多少可能的路径？
 * 
 * 说明：m 和 n 的值均不超过 100。
 * 
 * 示例 1:
 * 
 * 输入: m = 3, n = 2
 * 输出: 3
 * 解释:
 * 从左上角开始，总共有 3 条路径可以到达右下角。
 * 1. 向右 -> 向右 -> 向下
 * 2. 向右 -> 向下 -> 向右
 * 3. 向下 -> 向右 -> 向右
 * 
 * 
 * 示例 2:
 * 
 * 输入: m = 7, n = 3
 * 输出: 28
 * 
 */
public class Solution {
    private Dictionary<string,int> _cache = new Dictionary<string,int>();
    public int UniquePaths(int m, int n) {
        if(m == 1 || n == 1)
            return 1;
        string key = String.Format("{0}|{1}",m,n);
        if(_cache.ContainsKey(key))
            return _cache[key];
        _cache[key] = UniquePaths(m-1,n) + UniquePaths(m, n-1);
        return _cache[key];
    }
}


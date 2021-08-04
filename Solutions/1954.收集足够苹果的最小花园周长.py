#
# @lc app=leetcode.cn id=1954 lang=python3
#
# [1954] 收集足够苹果的最小花园周长
#
# https://leetcode-cn.com/problems/minimum-garden-perimeter-to-collect-enough-apples/description/
#
# algorithms
# Medium (48.54%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 7K
# Testcase Example:  '1'
#
# 给你一个用无限二维网格表示的花园，每一个 整数坐标处都有一棵苹果树。整数坐标 (i, j) 处的苹果树有 |i| + |j| 个苹果。
# 
# 你将会买下正中心坐标是 (0, 0) 的一块 正方形土地 ，且每条边都与两条坐标轴之一平行。
# 
# 给你一个整数 neededApples ，请你返回土地的 最小周长 ，使得 至少 有 neededApples 个苹果在土地 里面或者边缘上。
# 
# |x| 的值定义为：
# 
# 
# 如果 x >= 0 ，那么值为 x
# 如果 x < 0 ，那么值为 -x
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：neededApples = 1
# 输出：8
# 解释：边长长度为 1 的正方形不包含任何苹果。
# 但是边长为 2 的正方形包含 12 个苹果（如上图所示）。
# 周长为 2 * 4 = 8 。
# 
# 
# 示例 2：
# 
# 
# 输入：neededApples = 13
# 输出：16
# 
# 
# 示例 3：
# 
# 
# 输入：neededApples = 1000000000
# 输出：5040
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= neededApples <= 10^15
# 
# 
#

# @lc code=start
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        return bisect.bisect_left(list(map(lambda n: 2*n*(n+1)*(2*n+1), list(range(10**5)))), neededApples)*8
        
# @lc code=end


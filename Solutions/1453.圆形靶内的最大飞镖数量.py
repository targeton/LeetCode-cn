#
# @lc app=leetcode.cn id=1453 lang=python3
#
# [1453] 圆形靶内的最大飞镖数量
#
# https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/description/
#
# algorithms
# Hard (33.03%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    995
# Total Submissions: 3K
# Testcase Example:  '[[-2,0],[2,0],[0,2],[0,-2]]\n2'
#
# 墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。
# 
# 投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 r 。
# 
# 请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
# 输出：4
# 解释：如果圆形的飞镖靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
# 输出：5
# 解释：如果圆形的飞镖靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
# 
# 示例 3：
# 
# 输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
# 输出：1
# 
# 
# 示例 4：
# 
# 输入：points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= points.length <= 100
# points[i].length == 2
# -10^4 <= points[i][0], points[i][1] <= 10^4
# 1 <= r <= 5000
# 
# 
#

# @lc code=start
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def getCenter(pos1, pos2, r):
            res = []
            d = [pos2[0] - pos1[0], pos2[1] - pos1[1]]
            c = [pos1[0] + d[0]/2, pos1[1] + d[1]/2]
            D, R = (d[0]**2 + d[1]**2)/4, r**2
            if D > R:
                return res
            ratio = math.sqrt(R - D) / math.sqrt(D)
            v1, v2 = [c[0] - d[1] / 2 * ratio,  c[1] + d[0] / 2 * ratio], [c[0] + d[1] / 2 * ratio, c[1] - d[0] / 2 * ratio]
            return [v1, v2]

        res = 1
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                for cc in getCenter(points[i], points[j], r):
                    tmp = [p for p in points if ((p[0]-cc[0])**2 + (p[1]-cc[1])**2) <= r**2]
                    res = max(res, len(tmp))
        return res
# @lc code=end


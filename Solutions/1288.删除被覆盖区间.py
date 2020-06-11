#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#
# https://leetcode-cn.com/problems/remove-covered-intervals/description/
#
# algorithms
# Medium (55.81%)
# Likes:    10
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 4.6K
# Testcase Example:  '[[1,4],[3,6],[2,8]]'
#
# 给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
# 
# 只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
# 
# 在完成所有删除操作后，请你返回列表中剩余区间的数目。
# 
# 
# 
# 示例：
# 
# 
# 输入：intervals = [[1,4],[3,6],[2,8]]
# 输出：2
# 解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
# 
# 
# 
# 
# 提示：​​​​​​
# 
# 
# 1 <= intervals.length <= 1000
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# 对于所有的 i != j：intervals[i] != intervals[j]
# 
# 
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        if N < 2:
            return N
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        tmp, res = intervals[0], 1
        for i in range(1, N):
            if intervals[i][1] <= tmp[1]:
                continue
            tmp = intervals[i]
            res += 1
        return res

# @lc code=end


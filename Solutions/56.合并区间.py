#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (40.63%)
# Likes:    353
# Dislikes: 0
# Total Accepted:    70.2K
# Total Submissions: 171.2K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return intervals
        tmp = sorted(intervals,key = lambda x:(x[0],x[1]))
        res, i, t = [], 1, tmp[0]
        while i < len(tmp):
            if t[0] > tmp[i][1] or t[1] < tmp[i][0]:
                res.append(t)
                t = tmp[i]
            else:
                t=[min(tmp[i][0], t[0]),max(tmp[i][1], t[1])]
            i += 1
        res.append(t)
        return res                
        
# @lc code=end


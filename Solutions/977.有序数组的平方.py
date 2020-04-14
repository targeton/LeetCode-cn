#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.09%)
# Likes:    82
# Dislikes: 0
# Total Accepted:    33.3K
# Total Submissions: 46.8K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
# 
# 
# 
# 示例 1：
# 
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 
# 
# 示例 2：
# 
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。
# 
# 
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        j, N = 0, len(A)
        while j < N and A[j] < 0:
            j += 1
        i = j-1
        while i >= 0 and j < N:
            if A[i]**2 > A[j]**2:
                res.append(A[j]**2)
                j += 1
            else:
                res.append(A[i]**2)
                i -= 1
        while i >= 0:
            res.append(A[i]**2)
            i -= 1
        while j < N:
            res.append(A[j]**2)
            j += 1
        return res
# @lc code=end


#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#
# https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array/description/
#
# algorithms
# Easy (61.18%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 10.5K
# Testcase Example:  '[1,2,2,6,6,6,6,7,10]'
#
# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
# 
# 请你找到并返回这个整数
# 
# 
# 
# 示例：
# 
# 
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        span = N // 4 + 1
        for i in range(0, N, span):
            index_l = bisect.bisect_left(arr, arr[i])
            index_r = bisect.bisect_right(arr, arr[i])
            if index_r - index_l >= span:
                return arr[i]
        return -1
# @lc code=end


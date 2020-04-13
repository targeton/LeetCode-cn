#
# @lc app=leetcode.cn id=910 lang=python3
#
# [910] 最小差值 II
#
# https://leetcode-cn.com/problems/smallest-range-ii/description/
#
# algorithms
# Medium (26.78%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 9.2K
# Testcase Example:  '[1]\n0'
#
# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。
# 
# 在此过程之后，我们得到一些数组 B。
# 
# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
# 
# 
# 示例 2：
# 
# 输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
# 
# 
# 示例 3：
# 
# 输入：A = [1,3,6], K = 3
# 输出：3
# 解释：B = [4,6,3]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000
# 
# 
#

# @lc code=start
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mi, ma = A[0],A[-1]
        ans = ma - mi
        for i in range(len(A)-1):
            a,b = A[i],A[i+1]
            ans = min(ans, max(ma-K,a+K) - min(mi+K, b-K))
        return ans

# @lc code=end


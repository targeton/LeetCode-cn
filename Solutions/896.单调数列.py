#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#
# https://leetcode-cn.com/problems/monotonic-array/description/
#
# algorithms
# Easy (52.22%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 29K
# Testcase Example:  '[1,2,2,3]'
#
# 如果数组是单调递增或单调递减的，那么它是单调的。
# 
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A
# 是单调递减的。
# 
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,2,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：[6,5,4,4]
# 输出：true
# 
# 
# 示例 3：
# 
# 输入：[1,3,2]
# 输出：false
# 
# 
# 示例 4：
# 
# 输入：[1,2,4,5]
# 输出：true
# 
# 
# 示例 5：
# 
# 输入：[1,1,1]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
# 
# 
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        def cmp(x,y):
            return 0 if x == y else (1 if x > y else -1)
        
        flag = 0
        for i in range(len(A)-1):
            f = cmp(A[i],A[i+1])
            if f != 0:
                if f != flag and flag != 0:
                    return False
                flag = f
        return True
# @lc code=end


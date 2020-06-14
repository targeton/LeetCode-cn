#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (36.27%)
# Likes:    305
# Dislikes: 0
# Total Accepted:    32.1K
# Total Submissions: 88.3K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
# 
# 示例 1:
# 
# 输入: [10,2]
# 输出: 210
# 
# 示例 2:
# 
# 输入: [3,30,34,5,9]
# 输出: 9534330
# 
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(s1, s2):
            c1, c2 = s1+s2, s2+s1
            if c1 == c2:
                return 0
            elif c1 < c2:
                return -1
            else:
                return 1

        res = ''.join(sorted(map(str, nums), key=functools.cmp_to_key(cmp), reverse=True))
        return '0' if res[0] == '0' else res 
# @lc code=end


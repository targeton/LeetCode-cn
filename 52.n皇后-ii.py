#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (77.54%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 24.1K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
# 
# 示例:
# 
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
# [".Q..",  // 解法 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // 解法 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        nums = [-1]*n
        res = [0]
        self.dfs(nums, 0, res)
        return res[0]

    def dfs(self, nums, index, res):
        if len(nums) == index:
            res[0] += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.isValid(nums, index):
                self.dfs(nums, index+1, res)

    def isValid(self, nums, n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n-i or nums[i] == nums[n]:
                return False
        return True
# @lc code=end


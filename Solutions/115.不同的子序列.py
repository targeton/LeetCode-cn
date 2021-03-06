#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#
# https://leetcode-cn.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (49.40%)
# Likes:    299
# Dislikes: 0
# Total Accepted:    22.8K
# Total Submissions: 45.7K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# 
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE"
# 的一个子序列，而 "AEC" 不是）
# 
# 题目数据保证答案符合 32 位带符号整数范围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 
# 
# 示例 2：
# 
# 
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# (上箭头符号 ^ 表示选取的字母)
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
# 
# 
# 
# 提示：
# 
# 
# 0 
# s 和 t 由英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        cur, prev = [0]*(M+1), [0]*(M+1)
        cur[0], prev[0] = 1, 1
        for i in range(1, N+1):
            for j in range(1, M+1):
                if s[i-1] == t[j-1]:
                    cur[j] = prev[j-1] + prev[j]
                else:
                    cur[j] = prev[j]
            prev = list(cur)
        return cur[-1]
# @lc code=end


#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#
# https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
#
# algorithms
# Easy (66.53%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 17.8K
# Testcase Example:  '"bank"\n"kanb"'
#
# 给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。
# 
# 如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：s1 = "bank", s2 = "kanb"
# 输出：true
# 解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"
# 
# 
# 示例 2：
# 
# 输入：s1 = "attack", s2 = "defend"
# 输出：false
# 解释：一次字符串交换无法使两个字符串相等
# 
# 
# 示例 3：
# 
# 输入：s1 = "kelb", s2 = "kelb"
# 输出：true
# 解释：两个字符串已经相等，所以不需要进行字符串交换
# 
# 
# 示例 4：
# 
# 输入：s1 = "abcd", s2 = "dcba"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 和 s2 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N, M = len(s1), len(s2)
        if N != M:
            return False
        q = []
        for i in range(N):
            if s1[i] != s2[i]:
                q.append(i)
        if len(q) == 0:
            return True
        if len(q) != 2 or s1[q[0]] != s2[q[1]] or s1[q[1]] != s2[q[0]]:
            return False
        return True
# @lc code=end


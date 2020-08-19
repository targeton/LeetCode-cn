#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.68%)
# Likes:    2578
# Dislikes: 0
# Total Accepted:    350.3K
# Total Submissions: 1.1M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getRadius(s: str, l: int, r: int) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return (r - l - 2) // 2
        
        tmp = '#' + '#'.join(list(s)) + '#'
        radius = []
        idx, right = -1, -1
        end, start = -1, 0
        for i in range(len(tmp)):
            if i <= right:
                i_sym = 2*idx - i
                min_r = min(right - i, radius[i_sym])
                r = getRadius(tmp, i - min_r, i + min_r)
            else:
                r = getRadius(tmp, i, i)
            radius.append(r)
            if i + r > right:
                idx, right = i, i + r
            if 2 * r + 1 > end - start:
                start, end = i - r, i + r
        return tmp[start+1 : end : 2]
# @lc code=end


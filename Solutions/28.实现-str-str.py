#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (39.60%)
# Likes:    431
# Dislikes: 0
# Total Accepted:    162.6K
# Total Submissions: 409.9K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1

        next = [0]*len(needle)
        next[0] = -1
        i, j = 0, -1
        while i < len(needle)-1:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                if needle[i] == needle[j]:
                    next[i] = next[j]
                else:
                    next[i] = j
            else:
                j = next[j]               

        i, j, pos = 0,0,-1
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                j = next[j]
        if j >= len(needle):
            pos = i-len(needle)
        return pos
# @lc code=end


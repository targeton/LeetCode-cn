#
# @lc app=leetcode.cn id=1392 lang=python3
#
# [1392] 最长快乐前缀
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        next = [-1]*N
        for i in range(1,N):
            j = next[i-1]
            while j != -1 and s[j+1] != s[i]:
                j = next[j]
            if s[j+1] == s[i]:
                next[i] = j+1
        return s[:next[-1]+1]

# @lc code=end


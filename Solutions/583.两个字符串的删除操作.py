#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,M+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        sub = dp[N][M]
        return N+M-2*sub
# @lc code=end


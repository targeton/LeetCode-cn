#
# @lc app=leetcode.cn id=1563 lang=python3
#
# [1563] 石子游戏 V
#
# https://leetcode-cn.com/problems/stone-game-v/description/
#
# algorithms
# Hard (37.31%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 9.5K
# Testcase Example:  '[6,2,3,4,5,5]'
#
# 几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。
# 
# 游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob
# 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。
# 
# 只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。
# 
# 返回 Alice 能够获得的最大分数 。
# 
# 
# 
# 示例 1：
# 
# 输入：stoneValue = [6,2,3,4,5,5]
# 输出：18
# 解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice
# 的分数现在是 11 。
# 在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
# 最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 +
# 2）。游戏结束，因为这行只剩下一块石头了。
# 
# 
# 示例 2：
# 
# 输入：stoneValue = [7,7,7,7,7,7,7]
# 输出：28
# 
# 
# 示例 3：
# 
# 输入：stoneValue = [4]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= stoneValue.length <= 500
# 1 <= stoneValue[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        N = len(stoneValue)
        pre = [0]*(N+1)
        for i in range(N):
            pre[i+1] = pre[i]+stoneValue[i]
        
        dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
        
        for s in range(2,N+1):
            for i in range(N-s+1):
                j = i + s
                best = 0
                for k in range(i+1,j):
                    part1, part2 = pre[k]-pre[i], pre[j]-pre[k]
                    if part1 == part2:
                        best = max(best, part1 + max(dp[i][k], dp[k][j]))
                    elif part1 > part2:
                        best = max(best, part2 + dp[k][j])
                    else:
                        best = max(best, part1 + dp[i][k])
                dp[i][j] = best
        
        return dp[0][N]
# @lc code=end


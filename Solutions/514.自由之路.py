#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#
# https://leetcode-cn.com/problems/freedom-trail/description/
#
# algorithms
# Hard (40.98%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    12.7K
# Total Submissions: 26.2K
# Testcase Example:  '"godding"\n"gd"'
#
# 电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
# 
# 给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
# 
# 最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00
# 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
# 
# 旋转 ring 拼出 key 字符 key[i] 的阶段中：
# 
# 
# 您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符
# key[i] 。
# 如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key
# 的下一个字符（下一阶段）, 直至完成所有拼写。
# 
# 
# 示例：
# 
# 
# 
# 
# 
# 
# 
# 输入: ring = "godding", key = "gd"
# 输出: 4
# 解释:
# ⁠对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。 
# ⁠对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
# ⁠当然, 我们还需要1步进行拼写。
# ⁠因此最终的输出是 4。
# 
# 
# 提示：
# 
# 
# ring 和 key 的字符串长度取值范围均为 1 至 100；
# 两个字符串中都只有小写字符，并且均可能存在重复字符；
# 字符串 key 一定可以由字符串 ring 旋转拼出。
# 
# 
#

# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N, M = len(ring), len(key)
        dp = [[float('inf') for _ in range(N)] for _ in range(M)]
        pos = collections.defaultdict(list)
        for i,r in enumerate(ring):
            pos[r].append(i)
        
        for p in pos[key[0]]:
            dp[0][p] = min(p, N-p) + 1
        
        for i in range(1,M):
            for p in pos[key[i-1]]:
                for q in pos[key[i]]:
                    dp[i][q] = min(dp[i][q], dp[i-1][p] + min(abs(p-q), N-abs(p-q)) + 1)

        return min([dp[-1][i] for i in pos[key[-1]]])
        
# @lc code=end


#
# @lc app=leetcode.cn id=1871 lang=python3
#
# [1871] 跳跃游戏 VII
#
# https://leetcode-cn.com/problems/jump-game-vii/description/
#
# algorithms
# Medium (20.86%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 16.9K
# Testcase Example:  '"011010"\n2\n3'
#
# 给你一个下标从 0 开始的二进制字符串 s 和两个整数 minJump 和 maxJump 。一开始，你在下标 0 处，且该位置的值一定为 '0'
# 。当同时满足如下条件时，你可以从下标 i 移动到下标 j 处：
# 
# 
# i + minJump <= j <= min(i + maxJump, s.length - 1)  且 s[j] == '0'.
#  
# 
# 如果你可以到达 s 的下标 s.length - 1 处，请你返回 true ，否则返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "011010", minJump = 2, maxJump = 3
# 输出：true
# 解释：
# 第一步，从下标 0 移动到下标 3 。
# 第二步，从下标 3 移动到下标 5 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "01101110", minJump = 2, maxJump = 3
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= s.length <= 105
# s[i] 要么是 '0' ，要么是 '1'
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length
# 
# 
#

# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        N = len(s)
        pre, f = [0]*N, [0]*N
        f[0] = 1
        for i in range(minJump):
            pre[i] = 1
        for i in range(minJump, N):
            left, right = i-maxJump, i-minJump
            if s[i] == '0':
                tmp = pre[right] - (pre[left-1] if left > 0 else 0)
                f[i] = int(tmp != 0)
            pre[i] = pre[i-1] + f[i]
        return f[N-1] == 1
# @lc code=end


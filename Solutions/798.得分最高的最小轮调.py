#
# @lc app=leetcode.cn id=798 lang=python3
#
# [798] 得分最高的最小轮调
#
# https://leetcode-cn.com/problems/smallest-rotation-with-highest-score/description/
#
# algorithms
# Hard (45.77%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 2.4K
# Testcase Example:  '[2,3,1,4,0]'
#
# 给定一个数组 A，我们可以将它按一个非负整数 K 进行轮调，这样可以使数组变为 A[K], A[K+1], A{K+2], ... A[A.length
# - 1], A[0], A[1], ..., A[K-1] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。
# 
# 例如，如果数组为 [2, 4, 1, 3, 0]，我们按 K = 2 进行轮调后，它将变成 [1, 3, 0, 2, 4]。这将记作 3 分，因为 1 >
# 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4
# <= 4 [one point]。
# 
# 在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调索引 K。如果有多个答案，返回满足条件的最小的索引 K。
# 
# 
# 
# 示例 1：
# 
# 输入：[2, 3, 1, 4, 0]
# 输出：3
# 解释：
# 下面列出了每个 K 的得分：
# K = 0,  A = [2,3,1,4,0],    score 2
# K = 1,  A = [3,1,4,0,2],    score 3
# K = 2,  A = [1,4,0,2,3],    score 3
# K = 3,  A = [4,0,2,3,1],    score 4
# K = 4,  A = [0,2,3,1,4],    score 3
# 所以我们应当选择 K = 3，得分最高。
# 
# 示例 2：
# 
# 输入：[1, 3, 0, 2, 4]
# 输出：0
# 解释：
# A 无论怎么变化总是有 3 分。
# 所以我们将选择最小的 K，即 0。
# 
# 
# 
# 
# 提示：
# 
# 
# A 的长度最大为 20000。
# A[i] 的取值范围是 [0, A.length]。
# 
# 
#

# @lc code=start
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        N = len(nums)
        diff = [0 for _ in range(N+1)]
        for i,n in enumerate(nums):
            left, right = (i+1)%N, (i-n+1)%N
            diff[left] += 1
            diff[right] -= 1
            if left > right:
                diff[0] += 1
            # if n <= i:
            #     diff[0] += 1
            #     diff[i-n+1] -= 1
            #     diff[i+1] += 1
            #     diff[N] -= 1
            #     # for k in range(i-n+1):
            #     #     diff[k] += 1
            #     # for k in range(i+1, N):
            #     #     diff[k] += 1
            # else:
            #     diff[i+1] += 1
            #     diff[i+N-n+1] -= 1
            #     # for k in range(i+1, i+N-n+1):
            #     #     diff[k] += 1
        ma, pos, tmp = 0, 0, 0
        for i in range(N):
            tmp += diff[i]
            if tmp > ma:
                ma, pos = tmp, i
        return pos
# @lc code=end


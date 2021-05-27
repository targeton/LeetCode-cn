#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#
# https://leetcode-cn.com/problems/jump-game-iv/description/
#
# algorithms
# Hard (36.44%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 13.7K
# Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
#
# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。
# 
# 每一步，你可以从下标 i 跳到下标：
# 
# 
# i + 1 满足：i + 1 < arr.length
# i - 1 满足：i - 1 >= 0
# j 满足：arr[i] == arr[j] 且 i != j
# 
# 
# 请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。
# 
# 注意：任何时候你都不能跳到数组外面。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
# 
# 
# 示例 2：
# 
# 输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。
# 
# 
# 示例 3：
# 
# 输入：arr = [7,6,9,6,9,6,9,7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
# 
# 
# 示例 4：
# 
# 输入：arr = [6,1,9]
# 输出：2
# 
# 
# 示例 5：
# 
# 输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8
# 
# 
#

# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = collections.defaultdict(list)
        for i, n in enumerate(arr):
            dic[n].append(i)
        
        N = len(arr)
        target, s, ss, cnt, q = N-1, set([0]), set(), 0, [0]
        # s用于存储已bfs已搜索过的下标
        while target not in s:
            nq = []
            for pos in q:
                if pos-1 not in s and pos-1 >= 0:
                    nq.append(pos-1)
                    s.add(pos-1)
                if pos+1 not in s and pos+1 < N:
                    nq.append(pos+1)
                    s.add(pos+1)
                # ss用于存储已搜索过的元素值，防止bfs再次碰到同样元素值时再一次遍历同元素位置
                if arr[pos] not in ss:
                    for item in dic[arr[pos]]:
                        if item not in s:
                            nq.append(item)
                            s.add(item)
                    ss.add(arr[pos])
            cnt += 1
            q = nq
        return cnt

# @lc code=end
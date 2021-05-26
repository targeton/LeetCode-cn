#
# @lc app=leetcode.cn id=1306 lang=python3
#
# [1306] 跳跃游戏 III
#
# https://leetcode-cn.com/problems/jump-game-iii/description/
#
# algorithms
# Medium (57.59%)
# Likes:    71
# Dislikes: 0
# Total Accepted:    14.2K
# Total Submissions: 24.7K
# Testcase Example:  '[4,2,3,0,3,1,2]\n5'
#
# 这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i -
# arr[i]。
# 
# 请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。
# 
# 注意，不管是什么情况下，你都无法跳到数组之外。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [4,2,3,0,3,1,2], start = 5
# 输出：true
# 解释：
# 到达值为 0 的下标 3 有以下可能方案： 
# 下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
# 下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3 
# 
# 
# 示例 2：
# 
# 输入：arr = [4,2,3,0,3,1,2], start = 0
# 输出：true 
# 解释：
# 到达值为 0 的下标 3 有以下可能方案： 
# 下标 0 -> 下标 4 -> 下标 1 -> 下标 3
# 
# 
# 示例 3：
# 
# 输入：arr = [3,0,2,1,2], start = 2
# 输出：false
# 解释：无法到达值为 0 的下标 1 处。 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 5 * 10^4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length
# 
# 
#

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N, q = len(arr), [start]
        s = set(q)
        while q:
            pos = q.pop(0)
            if not arr[pos]:
                return True
            i, j = pos - arr[pos], pos + arr[pos]
            if i >= 0 and i not in s:
                q.append(i)
                s.add(i)
            if j < N and j not in s:
                q.append(j)
                s.add(j)
        return False
# @lc code=end


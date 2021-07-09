#
# @lc app=leetcode.cn id=930 lang=python3
#
# [面试题17.10] 主要元素
#
# https://leetcode-cn.com/problems/find-majority-element-lcci/
#
# algorithms
# Easy (XX.XX%)
# Likes:    XX
# Dislikes: XX
# Total Accepted:    XX
# Total Submissions: XX
# Testcase Example:  '[1,2,5,9,5,9,5,5,5]'
#
# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。
# 
# 请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[1,2,5,9,5,9,5,5,5]
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：[3,2]
# 输出：-1
# 
# 
# 输入: [2,2,1,1,1,2,2]
# 输出： 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      # 使用摩尔投票算法（Boyer-Moore），能够在时间复杂度O(n)，空间复杂度O(1)的要求下，找出主要元素。
      # 算法思想：每次从序列中选择两个不相同的数字删除掉（抵消），最后剩下一个数字或几个相同数字，就是出现次数大于总数一半的那个。
      candidate, cnt = -1, 0
      for n in nums:
        if cnt == 0:
          candidate = n
        if n == candidate:
          cnt += 1
        else:
          cnt -= 1
      if cnt == 0:
        return -1
      cnt = 0
      for n in nums:
        if n == candidate:
          cnt += 1
      return candidate if cnt*2 > len(nums) else -1

# @lc code=end
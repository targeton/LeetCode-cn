#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
# https://leetcode-cn.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (37.19%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 16.8K
# Testcase Example:  '[1,2,3]'
#
# 给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si =
# 0。
# 
# 如果有多个目标子集，返回其中任何一个均可。
# 
# 
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2] (当然, [1,3] 也正确)
# 
# 
# 示例 2:
# 
# 输入: [1,2,4,8]
# 输出: [1,2,4,8]
# 
# 
#

# @lc code=start

# ths solution is to find the one with most factors
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dic = collections.defaultdict(list)
        dic[nums[0]].append(nums[0])
        res = nums[:1]
        for i in range(1, len(nums)):
            tmp = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(tmp) < len(dic[nums[j]]):
                        tmp = dic[nums[j]][:]
            tmp.append(nums[i])
            dic[nums[i]] = tmp
            if len(res) < len(tmp):
                res = tmp
        return res

        
# @lc code=end


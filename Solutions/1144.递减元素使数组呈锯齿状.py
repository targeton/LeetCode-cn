#
# @lc app=leetcode.cn id=1144 lang=python3
#
# [1144] 递减元素使数组呈锯齿状
#

# @lc code=start
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if not nums:
            return 0
        step0, prev0, step1, prev1 = 0, nums[0], 0, nums[0]
        for i in range(1,len(nums)):
            if i % 2:
                if nums[i] <= prev1:
                    step1 += prev1 - nums[i] + 1
                prev1 = nums[i]
                
                if nums[i] >= prev0:
                    step0 += nums[i] - prev0 + 1
                    nums[i] = prev0 - 1
                prev0 = nums[i]
            else:
                if nums[i] <= prev0:
                    step0 += prev0 - nums[i] + 1
                prev0 = nums[i]

                if nums[i] >= prev1:
                    step1 += nums[i] - prev1 + 1
                    nums[i] = prev1 - 1
                prev1 = nums[i]
        
        return min(step0, step1)

# @lc code=end


#
# @lc app=leetcode.cn id=1707 lang=python3
#
# [1707] 与数组中元素的最大异或值
#
# https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array/description/
#
# algorithms
# Hard (33.10%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    704
# Total Submissions: 2.1K
# Testcase Example:  '[0,1,2,3,4]\n[[3,1],[1,3],[5,6]]'
#
# 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。
# 
# 第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR
# xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。
# 
# 返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i
# 个查询的答案。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# 输出：[3,3,7]
# 解释：
# 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
# 
# 
# 示例 2：
# 
# 输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# 输出：[15,-1,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length, queries.length <= 10^5
# queries[i].length == 2
# 0 <= nums[j], xi, mi <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = {}
        for num in nums:
            p = trie
            for i in range(31,-1,-1):
                bit = 1 if num & (1<<i) else 0
                if bit not in p:
                    p[bit] = [{}, float('inf')]
                p[bit][1] = min(p[bit][1], num)
                p = p[bit][0]
        
        res = []
        for x,limit in queries:
            ans = 0
            p = trie
            for i in range(31,-1,-1):
                if x & (1<<i):
                    if 0 in p:
                        ans ^= 1<<i
                        p = p[0][0]
                    elif 1 not in p or p[1][1] > limit:
                        res.append(-1)
                        break
                    else:
                        p = p[1][0]
                else:
                    if 1 in p and p[1][1] <= limit:
                        ans ^= 1<<i
                        p = p[1][0]
                    elif 0 not in p:
                        res.append(-1)
                        break
                    else:
                        p = p[0][0]
            if not i:
                res.append(ans)
        return res
# @lc code=end


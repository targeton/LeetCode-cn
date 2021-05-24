#
# @lc app=leetcode.cn id=1404 lang=python3
#
# [1404] 将二进制表示减到 1 的步骤数
#
# https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
#
# algorithms
# Medium (48.79%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 13.6K
# Testcase Example:  '"1101"'
#
# 给你一个以二进制形式表示的数字 s 。请你返回按下述规则将其减少到 1 所需要的步骤数：
# 
# 
# 
# 如果当前数字为偶数，则将其除以 2 。
# 
# 
# 如果当前数字为奇数，则将其加上 1 。
# 
# 
# 
# 题目保证你总是可以按上述规则将测试用例变为 1 。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "1101"
# 输出：6
# 解释："1101" 表示十进制数 13 。
# Step 1) 13 是奇数，加 1 得到 14 
# Step 2) 14 是偶数，除 2 得到 7
# Step 3) 7  是奇数，加 1 得到 8
# Step 4) 8  是偶数，除 2 得到 4  
# Step 5) 4  是偶数，除 2 得到 2 
# Step 6) 2  是偶数，除 2 得到 1  
# 
# 
# 示例 2：
# 
# 输入：s = "10"
# 输出：1
# 解释："10" 表示十进制数 2 。
# Step 1) 2 是偶数，除 2 得到 1 
# 
# 
# 示例 3：
# 
# 输入：s = "1"
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 500
# s 由字符 '0' 或 '1' 组成。
# s[0] == '1'
# 
# 
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        N = len(s)
        ans, meet1 = 0, False
        for i in range(N-1,-1,-1):
            if s[i] == '0':
                ans += 2 if meet1 else 1
            else:
                if meet1:
                    ans += 1
                else:
                    if i:
                        ans += 2
                    meet1 = True
        return ans
# @lc code=end


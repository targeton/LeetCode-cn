#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
# https://leetcode-cn.com/problems/additive-number/description/
#
# algorithms
# Medium (32.33%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 24.8K
# Testcase Example:  '"112358"'
#
# 累加数是一个字符串，组成它的数字可以形成累加序列。
# 
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
# 
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
# 
# 示例 1:
# 
# 输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# 示例 2:
# 
# 输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 
# 进阶:
# 你如何处理一个溢出的过大的整数输入?
# 
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        def add(op1: str, op2: str) -> str:
            s1, s2 = list(op1), list(op2)
            res, flag = [], 0
            while s1 or s2:
                t1 = ord(s1.pop()) - ord('0') if s1 else 0
                t2 = ord(s2.pop()) - ord('0') if s2 else 0
                tmp = t1 + t2 + flag
                res.insert(0, tmp % 10)
                flag = tmp // 10
            if flag:
                res.insert(0, flag)
            return ''.join(map(str, res))        

        def check(pos0: int, pos1: int, pos2: int) -> bool:
            if pos2 == N:
                return True
            if pos2 + max(pos2-pos1, pos1-pos0) > N:
                return False
            if pos1 - pos0 > 1 and num[pos0] == '0' \
                or pos2 - pos1 > 1 and num[pos1] == '0':
                return False
            tmp = add(num[pos0:pos1], num[pos1:pos2])
            span = len(tmp)
            if pos2 + span > N:
                return False
            if tmp == num[pos2:pos2+span]:
                return True and check(pos1, pos2, pos2+span)
            return False
        
        for i in range(2, N):
            for j in range(i):
                if not check(0, j, i):
                    continue
                return True
        return False

# @lc code=end


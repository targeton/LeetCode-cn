#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (26.41%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    11.7K
# Total Submissions: 44.4K
# Testcase Example:  '1\n2'
#
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
# 
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 
# 示例 1:
# 
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 
# 
# 示例 2:
# 
# 输入: numerator = 2, denominator = 1
# 输出: "2"
# 
# 示例 3:
# 
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"
# 
# 
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = numerator // denominator
        n, d = abs(numerator), abs(denominator)   
        res = str(n // d) if flag >= 0 else '-' + str(n//d)
        r, tmp, dic, index = n % d, '', {}, 0
        while r:
            if r in dic:
                tmp = tmp[:dic[r]] + '(' + tmp[dic[r]:] + ')'
                break
            dic[r] = index
            r *= 10
            tmp += str(r // d)
            r %= d
            index += 1
        return res if not tmp else '.'.join([res, tmp])
# @lc code=end


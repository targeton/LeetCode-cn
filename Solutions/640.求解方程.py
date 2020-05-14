#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#
# https://leetcode-cn.com/problems/solve-the-equation/description/
#
# algorithms
# Medium (40.24%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 11.7K
# Testcase Example:  '"x+5-3+x=6+x-2"'
#
# 求解一个给定的方程，将x以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量 x 和其对应系数。
# 
# 如果方程没有解，请返回“No solution”。
# 
# 如果方程有无限解，则返回“Infinite solutions”。
# 
# 如果方程中只有一个解，要保证返回值 x 是一个整数。
# 
# 示例 1：
# 
# 输入: "x+5-3+x=6+x-2"
# 输出: "x=2"
# 
# 
# 示例 2:
# 
# 输入: "x=x"
# 输出: "Infinite solutions"
# 
# 
# 示例 3:
# 
# 输入: "2x=x"
# 输出: "x=0"
# 
# 
# 示例 4:
# 
# 输入: "2x+3x-6x=x+2"
# 输出: "x=-1"
# 
# 
# 示例 5:
# 
# 输入: "x=x+2"
# 输出: "No solution"
# 
# 
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        def coffe(s):
            if len(s) > 1 and '0' <= s[-2] <= '9':
                return s.replace('x', '')
            return s.replace('x', '1')

        arr = equation.split('=')
        lhs, rhs = 0, 0
        for s in re.split(r'(?=\+)|(?=-)', arr[0]):
            if s.count('x') > 0:
                lhs += int(coffe(s))
            else:
                rhs -= int(s)
        for s in re.split(r'(?=\+)|(?=-)', arr[1]):
            if s.count('x') > 0:
                lhs -= int(coffe(s))
            else:
                rhs += int(s)
        
        if not lhs:
            if not rhs:
                return 'Infinite solutions'
            else:
                return 'No solution'
        return 'x=%d'%(rhs//lhs)

# @lc code=end


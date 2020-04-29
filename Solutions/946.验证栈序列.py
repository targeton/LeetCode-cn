#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
# https://leetcode-cn.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (55.18%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 16.6K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop
# 操作序列的结果时，返回 true；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# 
# 
# 示例 2：
# 
# 输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed 是 popped 的排列。
# 
# 
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) < 1:
            return True
        tmp = [pushed.pop(0)]
        while pushed or popped:
            while tmp and popped and tmp[-1] == popped[0]:
                tmp.pop()
                popped.pop(0)
            if pushed:
                tmp.append(pushed.pop(0))
            else:
                break

        if not tmp and not popped:
            return True
        else:
            return False        
# @lc code=end


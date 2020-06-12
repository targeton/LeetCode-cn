#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (37.82%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    55.8K
# Total Submissions: 147.4K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        N = len(t)
        tmp, mi = [], len(s)+1
        res = ''
        for i,ch in enumerate(s):
            if ch not in counter:
                continue
            tmp.append(i)
            if counter[ch] > 0:
                N -= 1
            counter[ch] -= 1
            while not N:
                span = tmp[-1] - tmp[0] + 1
                if span < mi:
                    mi = span
                    res = s[tmp[0]: tmp[-1]+1]
                first = tmp.pop(0)
                counter[s[first]] += 1
                if counter[s[first]] > 0:
                    N += 1
        
        return res
                

# @lc code=end


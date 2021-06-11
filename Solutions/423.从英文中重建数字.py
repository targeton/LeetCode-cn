#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#
# https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (56.62%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 12.8K
# Testcase Example:  '"owoztneoer"'
#
# 给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。
# 
# 注意:
# 
# 
# 输入只包含小写英文字母。
# 输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
# 输入字符串的长度小于 50,000。
# 
# 
# 示例 1:
# 
# 
# 输入: "owoztneoer"
# 
# 输出: "012" (zeroonetwo)
# 
# 
# 示例 2:
# 
# 
# 输入: "fviefuro"
# 
# 输出: "45" (fourfive)
# 
# 
#

# @lc code=start
class Solution:
    def originalDigits(self, s: str) -> str:
        # zero, one, two, three, four, five, six, seven, eight, nine
        ans = [0 for _ in range(10)]
        cnt = [0 for _ in range(26)]
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        ans[0] = cnt[ord('z')-ord('a')]
        ans[2] = cnt[ord('w')-ord('a')]
        ans[4] = cnt[ord('u')-ord('a')]
        ans[6] = cnt[ord('x')-ord('a')]
        ans[8] = cnt[ord('g')-ord('a')]
        ans[7] = cnt[ord('s')-ord('a')] - ans[6]
        ans[5] = cnt[ord('v')-ord('a')] - ans[7]
        ans[3] = cnt[ord('t')-ord('a')] - ans[2] - ans[8]
        ans[1] = cnt[ord('o')-ord('a')] - ans[0] - ans[2] - ans[4]
        ans[9] = cnt[ord('i')-ord('a')] - ans[5] - ans[6] - ans[8]

        res = ""
        for i in range(10):
            res += str(i)*ans[i]
        return res    
# @lc code=end


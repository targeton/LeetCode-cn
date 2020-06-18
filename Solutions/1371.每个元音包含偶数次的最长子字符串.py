#
# @lc app=leetcode.cn id=1371 lang=python3
#
# [1371] 每个元音包含偶数次的最长子字符串
#
# https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
#
# algorithms
# Medium (58.48%)
# Likes:    247
# Dislikes: 0
# Total Accepted:    15.5K
# Total Submissions: 26.4K
# Testcase Example:  '"eleetminicoworoep"'
#
# 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u'
# ，在子字符串中都恰好出现了偶数次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "eleetminicoworoep"
# 输出：13
# 解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "leetcodeisgreat"
# 输出：5
# 解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "bcbcbc"
# 输出：6
# 解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 5 x 10^5
# s 只包含小写英文字母。
# 
# 
#

# @lc code=start
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        status = [float('inf')] * 32
        status[0] = 0
        flag, ans = 0, 0
        for i,ch in enumerate(s):
            if ch in d:
                flag ^= 1 << d[ch]
            if status[flag] != float('inf'):
                ans = max(ans, i+1-status[flag])
            else:
                status[flag] = i+1
        return ans        
        
# @lc code=end


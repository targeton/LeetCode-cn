#
# @lc app=leetcode.cn id=1722 lang=python3
#
# [1722] 执行交换操作后的最小汉明距离
#
# https://leetcode-cn.com/problems/minimize-hamming-distance-after-swap-operations/description/
#
# algorithms
# Medium (51.79%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 8.3K
# Testcase Example:  '[1,2,3,4]\n[2,1,4,5]\n[[0,1],[2,3]]'
#
# 给你两个整数数组 source 和 target ，长度都是 n 。还有一个数组 allowedSwaps ，其中每个 allowedSwaps[i] =
# [ai, bi] 表示你可以交换数组 source 中下标为 ai 和 bi（下标从 0 开始）的两个元素。注意，你可以按 任意 顺序 多次
# 交换一对特定下标指向的元素。
# 
# 相同长度的两个数组 source 和 target 间的 汉明距离 是元素不同的下标数量。形式上，其值等于满足 source[i] !=
# target[i] （下标从 0 开始）的下标 i（0 <= i <= n-1）的数量。
# 
# 在对数组 source 执行 任意 数量的交换操作后，返回 source 和 target 间的 最小汉明距离 。
# 
# 
# 
# 示例 1：
# 
# 输入：source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# 输出：1
# 解释：source 可以按下述方式转换：
# - 交换下标 0 和 1 指向的元素：source = [2,1,3,4]
# - 交换下标 2 和 3 指向的元素：source = [2,1,4,3]
# source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。
# 
# 
# 示例 2：
# 
# 输入：source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# 输出：2
# 解释：不能对 source 执行交换操作。
# source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。
# 
# 示例 3：
# 
# 输入：source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps =
# [[0,4],[4,2],[1,3],[1,4]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# n == source.length == target.length
# 1 <= n <= 10^5
# 1 <= source[i], target[i] <= 10^5
# 0 <= allowedSwaps.length <= 10^5
# allowedSwaps[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# 
# 
#

# @lc code=start

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = {i:i for i in range(n)}

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        for l, r in allowedSwaps:
            a, b = find(l), find(r)
            if a != b:
                parent[b] = a
        
        dic = collections.defaultdict(list)
        for i in range(n):
            a = find(i)
            dic[a].append(i)
        
        res = 0
        for k,v in dic.items():
            a = [source[i] for i in v]
            b = Counter([target[i] for i in v])
            for c in a:
                if b[c] > 0:
                    b[c] -= 1
                else:
                    res += 1
        return res
# @lc code=end


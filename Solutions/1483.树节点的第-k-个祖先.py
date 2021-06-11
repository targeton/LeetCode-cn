#
# @lc app=leetcode.cn id=1483 lang=python3
#
# [1483] 树节点的第 K 个祖先
#
# https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node/description/
#
# algorithms
# Hard (29.67%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 9.8K
# Testcase Example:  '["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]\n' +
  '[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]'
#
# 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为
# 0 的节点。
# 
# 请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k
# 个祖先节点。如果不存在这样的祖先节点，返回 -1 。
# 
# 树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：
# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
# 
# 输出：
# [null,1,0,-1]
# 
# 解释：
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
# 
# treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
# treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
# treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= n <= 5*10^4
# parent[0] == -1 表示编号为 0 的节点是根节点。
# 对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
# 0 <= node < n
# 至多查询 5*10^4 次
# 
# 
#

# @lc code=start
class TreeAncestor:
    # The following recursive formula is the core logic
    # dp[i][j] = dp[dp[i][j-1]][j-1]
    def __init__(self, n: int, parent: List[int]):
      self.dp = [[] for _ in range(n)]
      q = []
      for i in range(n):
        self.dp[i].append(parent[i])
        if self.dp[i][-1] != -1:
          q.append(i)

      for j in range(1,n):
        allneg = True
        for i in range(n):
          t = -1 if self.dp[i][j-1] == -1 else self.dp[self.dp[i][j-1]][j-1]
          self.dp[i].append(t)
          if t != -1:
            allneg = False
        if allneg:
          break

    def getKthAncestor(self, node: int, k: int) -> int:
      res, pos = node, 0
      while k and res != -1:
        if pos >= len(self.dp[res]):
          return -1
        if k & 1:
          res = self.dp[res][pos]
        k >>= 1
        pos += 1
      return res


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# @lc code=end

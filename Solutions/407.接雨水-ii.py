#
# @lc app=leetcode.cn id=407 lang=python3
#
# [407] 接雨水 II
#
# https://leetcode-cn.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (39.80%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 9.3K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
# 
# 
# 
# 示例：
# 
# 给出如下 3x6 的高度图:
# [
# ⁠ [1,4,3,1,3,2],
# ⁠ [3,2,1,3,2,4],
# ⁠ [2,3,3,2,3,1]
# ]
# 
# 返回 4 。
# 
# 
# 
# 
# 如上图所示，这是下雨前的高度图[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 的状态。
# 
# 
# 
# 
# 
# 下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 110
# 0 <= heightMap[i][j] <= 20000
# 
# 
#

# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])
        heap = []
        visited = set()
        for i in [0, M-1]:
            for j in range(N):
                heap.append((heightMap[i][j], i, j))
                visited.add((i, j))
        for j in [0, N-1]:
            for i in range(M):
                heap.append((heightMap[i][j], i, j))
                visited.add((i, j))
        
        dxy = [[-1,0], [0,-1], [1,0], [0,1]]
        heapq.heapify(heap)
        res = 0
        while heap:
            h, x, y = heapq.heappop(heap)
            for dx,dy in dxy:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < M and 0 <= ny < N):
                    continue
                if (nx, ny) in visited:
                    continue
                if h > heightMap[nx][ny]:
                    res += h-heightMap[nx][ny]
                heapq.heappush(heap, (max(h, heightMap[nx][ny]), nx, ny))
                visited.add((nx, ny))
        return res
# @lc code=end


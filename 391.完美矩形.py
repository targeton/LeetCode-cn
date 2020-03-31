#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#
# https://leetcode-cn.com/problems/perfect-rectangle/description/
#
# algorithms
# Hard (25.24%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 4.5K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
# 我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。
# 
# 每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1)
# 以及右上角的点的坐标为 (2, 2) )。
# 
# 
# 
# 示例 1:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4],
# ⁠ [1,3,2,4],
# ⁠ [2,3,3,4]
# ]
# 
# 返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
# 
# 
# 
# 
# 
# 
# 示例 2:
# 
# rectangles = [
# ⁠ [1,1,2,3],
# ⁠ [1,3,2,4],
# ⁠ [3,1,4,2],
# ⁠ [3,2,4,4]
# ]
# 
# 返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
# 
# 
# 
# 
# 
# 
# 示例 3:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [3,2,4,4]
# ]
# 
# 返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
# 
# 
# 
# 
# 
# 
# 示例 4:
# 
# rectangles = [
# ⁠ [1,1,3,3],
# ⁠ [3,1,4,2],
# ⁠ [1,3,2,4],
# ⁠ [2,2,4,4]
# ]
# 
# 返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
# 
# 
#

# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        lookup = set()
        x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')
        area = 0
        # calculate sum of all rectangles's area, and judge whether the four vertices of any rectangle conincide with other rectangles's vertices
        for xx1, yy1, xx2, yy2 in rectangles:
            for item in [(xx1,yy1), (xx1,yy2), (xx2,yy1), (xx2,yy2)]:
                if item in lookup:
                    lookup.remove(item)
                else:
                    lookup.add(item)
            area += (xx2-xx1)*(yy2-yy1)
            x1, y1, x2, y2 = min(x1,xx1), min(y1,yy1), max(x2,xx2), max(y2,yy2)
        
        if len(lookup) != 4 or (x1,y1) not in lookup or (x1,y2) not in lookup or (x2,y1) not in lookup or (x2,y2) not in lookup:
            return False
        
        return area == (x2-x1)*(y2-y1)
# @lc code=end


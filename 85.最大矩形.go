/*
 * @lc app=leetcode.cn id=85 lang=golang
 *
 * [85] 最大矩形
 *
 * https://leetcode-cn.com/problems/maximal-rectangle/description/
 *
 * algorithms
 * Hard (44.44%)
 * Likes:    154
 * Dislikes: 0
 * Total Accepted:    5K
 * Total Submissions: 11.3K
 * Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
 *
 * 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
 *
 * 示例:
 *
 * 输入:
 * [
 * ⁠ ["1","0","1","0","0"],
 * ⁠ ["1","0","1","1","1"],
 * ⁠ ["1","1","1","1","1"],
 * ⁠ ["1","0","0","1","0"]
 * ]
 * 输出: 6
 *
 */
func maximalRectangle(matrix [][]byte) int {
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	m, n := len(matrix), len(matrix[0])
	h := make([]int, n+1)
	max := 0
	for i := 0; i < m; i++ {
		s := make([]int, 0)
		for j := 0; j < n; j++ {
			if matrix[i][j] == '1' {
				h[j]++
			} else {
				h[j] = 0
			}
		}
		for k := 0; k < n+1; {
			l := 0
			if k < n {
				l = h[k]
			}
			if len(s) == 0 || l > h[s[len(s)-1]] {
				s = append(s, k)
				k++
			} else {
				tp := s[len(s)-1]
				s = s[:len(s)-1]
				w := 0
				if len(s) == 0 {
					w = k
				} else {
					w = k - s[len(s)-1] - 1
				}
				area := w * h[tp]
				if area > max {
					max = area
				}
			}
		}
	}
	return max
}

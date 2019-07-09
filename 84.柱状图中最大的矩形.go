/*
 * @lc app=leetcode.cn id=84 lang=golang
 *
 * [84] 柱状图中最大的矩形
 *
 * https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
 *
 * algorithms
 * Hard (38.14%)
 * Likes:    195
 * Dislikes: 0
 * Total Accepted:    8.3K
 * Total Submissions: 21.8K
 * Testcase Example:  '[2,1,5,6,2,3]'
 *
 * 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
 *
 * 求在该柱状图中，能够勾勒出来的矩形的最大面积。
 *
 *
 *
 *
 *
 * 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
 *
 *
 *
 *
 *
 * 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
 *
 *
 *
 * 示例:
 *
 * 输入: [2,1,5,6,2,3]
 * 输出: 10
 *
 */
func largestRectangleArea(heights []int) int {
	lessFromLeft := make([]int, len(heights))
	lessFromRight := make([]int, len(heights))
	for i := 0; i < len(heights); i++ {
		p := i - 1
		for p >= 0 && heights[p] >= heights[i] {
			p = lessFromLeft[p]
		}
		lessFromLeft[i] = p
	}
	for j := len(heights) - 1; j >= 0; j-- {
		q := j + 1
		for q < len(heights) && heights[q] >= heights[j] {
			q = lessFromRight[q]
		}
		lessFromRight[j] = q
	}
	max := 0
	for k := 0; k < len(heights); k++ {
		area := (lessFromRight[k] - lessFromLeft[k] - 1) * heights[k]
		if area > max {
			max = area
		}
	}
	return max
}

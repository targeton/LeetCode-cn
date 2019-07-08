/*
 * @lc app=leetcode.cn id=103 lang=golang
 *
 * [103] 二叉树的锯齿形层次遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
 *
 * algorithms
 * Medium (50.05%)
 * Likes:    74
 * Dislikes: 0
 * Total Accepted:    13K
 * Total Submissions: 25.9K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
 *
 * 例如：
 * 给定二叉树 [3,9,20,null,null,15,7],
 *
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 *
 *
 * 返回锯齿形层次遍历如下：
 *
 * [
 * ⁠ [3],
 * ⁠ [20,9],
 * ⁠ [15,7]
 * ]
 *
 *
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	var res [][]int
	helper(&res, root, 0)
	return res
}

func helper(res *[][]int, node *TreeNode, height int) {
	if node == nil {
		return
	}
	if len(*res) == height {
		*res = append(*res, []int{})
	}
	if height%2 == 0 {
		(*res)[height] = append((*res)[height], node.Val)
	} else {
		(*res)[height] = append([]int{node.Val}, (*res)[height]...)
	}
	if node.Left != nil {
		helper(res, node.Left, height+1)
	}
	if node.Right != nil {
		helper(res, node.Right, height+1)
	}
}

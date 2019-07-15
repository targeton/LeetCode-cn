/*
 * @lc app=leetcode.cn id=79 lang=golang
 *
 * [79] 单词搜索
 *
 * https://leetcode-cn.com/problems/word-search/description/
 *
 * algorithms
 * Medium (37.95%)
 * Likes:    153
 * Dislikes: 0
 * Total Accepted:    13.3K
 * Total Submissions: 34.9K
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
 *
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 *
 * 示例:
 *
 * board =
 * [
 * ⁠ ['A','B','C','E'],
 * ⁠ ['S','F','C','S'],
 * ⁠ ['A','D','E','E']
 * ]
 *
 * 给定 word = "ABCCED", 返回 true.
 * 给定 word = "SEE", 返回 true.
 * 给定 word = "ABCB", 返回 false.
 *
 */
func exist(board [][]byte, word string) bool {
	if board == nil || len(board) < 1 {
		return false
	}
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if isExist(board, word, 0, i, j) {
				return true
			}
		}
	}
	return false
}

func isExist(board [][]byte, word string, pos, i, j int) bool {
	if pos == len(word) {
		return true
	}
	if i < 0 || i >= len(board) || j < 0 || j >= len(board[0]) {
		return false
	}
	if board[i][j] == word[pos] {
		board[i][j] ^= byte(255)
		exist := isExist(board, word, pos+1, i-1, j) || isExist(board, word, pos+1, i, j-1) || isExist(board, word, pos+1, i+1, j) || isExist(board, word, pos+1, i, j+1)
		board[i][j] ^= byte(255)
		return exist
	} else {
		return false
	}
}

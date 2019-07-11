/*
 * @lc app=leetcode.cn id=17 lang=golang
 *
 * [17] 电话号码的字母组合
 *
 * https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (49.85%)
 * Likes:    365
 * Dislikes: 0
 * Total Accepted:    30.6K
 * Total Submissions: 61.4K
 * Testcase Example:  '"23"'
 *
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
 *
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 *
 *
 *
 * 示例:
 *
 * 输入："23"
 * 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 *
 *
 * 说明:
 * 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
 *
 */
func letterCombinations(digits string) []string {
	cache := map[byte]string{'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
	var res []string
	if len(digits) < 1 {
		return res
	}
	combination(&res, &cache, digits, "", 0)
	return res
}

func combination(res *[]string, cache *map[byte]string, digits string, tmp string, pos int) {
	if len(digits) == pos {
		*res = append(*res, tmp)
		return
	}
	for i := 0; i < len((*cache)[digits[pos]]); i++ {
		combination(res, cache, digits, tmp+string((*cache)[digits[pos]][i]), pos+1)
	}
}

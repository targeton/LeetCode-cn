/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (23.04%)
 * Likes:    1145
 * Dislikes: 0
 * Total Accepted:    69.8K
 * Total Submissions: 301.7K
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
 * ？找出所有满足条件且不重复的三元组。
 *
 * 注意：答案中不可以包含重复的三元组。
 *
 * 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
 *
 * 满足要求的三元组集合为：
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 *
 *
 */
func threeSum(nums []int) [][]int {
	res := make([][]int, 0)
	if nums == nil || len(nums) < 3 {
		return res
	}
	sort(nums)
	for i := 0; i < len(nums)-2; i++ {
		if i == 0 || nums[i] != nums[i-1] {
			p, q := i+1, len(nums)-1
			t := 0 - nums[i]
			for p < q {
				if nums[p]+nums[q] == t {
					res = append(res, []int{nums[i], nums[p], nums[q]})
					for p < q && nums[p] == nums[p+1] {
						p++
					}
					for p < q && nums[q] == nums[q-1] {
						q--
					}
					p++
					q--
				} else if nums[p]+nums[q] > t {
					q--
				} else {
					p++
				}
			}
		}

	}
	return res
}

func sort(nums []int) {
	if nums == nil || len(nums) <= 1 {
		return
	}
	head, tail, i := 0, len(nums)-1, 1
	for head < tail {
		if nums[head] < nums[tail] {
			tail--
		} else {
			nums[head], nums[tail], nums[i] = nums[tail], nums[i], nums[head]
			head++
			i++
		}
	}
	sort(nums[:head])
	sort(nums[head+1:])
}

/*
 * @lc app=leetcode.cn id=46 lang=csharp
 *
 * [46] 全排列
 *
 * https://leetcode-cn.com/problems/permutations/description/
 *
 * algorithms
 * Medium (71.85%)
 * Likes:    511
 * Dislikes: 0
 * Total Accepted:    74.4K
 * Total Submissions: 100.8K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个没有重复数字的序列，返回其所有可能的全排列。
 * 
 * 示例:
 * 
 * 输入: [1,2,3]
 * 输出:
 * [
 * ⁠ [1,2,3],
 * ⁠ [1,3,2],
 * ⁠ [2,1,3],
 * ⁠ [2,3,1],
 * ⁠ [3,1,2],
 * ⁠ [3,2,1]
 * ]
 * 
 */

// @lc code=start
public class Solution {
    public IList<IList<int>> Permute(int[] nums) {
        var result = new List<IList<int>>();
        Backtrack(nums.Length, nums.ToList<int>(), result, 0);
        return result;
    }

    private void Backtrack(int n, IList<int> input, IList<IList<int>> output, int first){
        if(first == n)
            output.Add(new List<int>(input));
        for (int i = first; i < input.Count; i++)
        {
            input.Swap<int>(first, i);
            Backtrack(n, input, output, first + 1);
            input.Swap<int>(first, i);           
        }
    }
}

public static class Extension {
    public static void Swap<T>(this IList<T> list,int index0,int index1){
        T tmp = list[index0];
        list[index0] = list[index1];
        list[index1] = tmp;
    }
}
// @lc code=end


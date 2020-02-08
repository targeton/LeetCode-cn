/*
 * @lc app=leetcode.cn id=47 lang=csharp
 *
 * [47] 全排列 II
 *
 * https://leetcode-cn.com/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (54.24%)
 * Likes:    215
 * Dislikes: 0
 * Total Accepted:    36.7K
 * Total Submissions: 64.6K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个可包含重复数字的序列，返回所有不重复的全排列。
 * 
 * 示例:
 * 
 * 输入: [1,1,2]
 * 输出:
 * [
 * ⁠ [1,1,2],
 * ⁠ [1,2,1],
 * ⁠ [2,1,1]
 * ]
 * 
 */

// @lc code=start
public class Solution {
    public IList<IList<int>> PermuteUnique(int[] nums) {
        var result = new List<IList<int>>();
        Backtrack(nums.Length, nums.ToList<int>(), result, 0);
        return result;
    }

    private void Backtrack(int n, IList<int> input, IList<IList<int>> output, int first){
        if(first == n)
            output.Add(new List<int>(input));
        var set = new HashSet<int>();
        for (int i = first; i < input.Count; i++)
        {
            if(set.Contains(input[i]))
                continue;
            input.Swap<int>(first, i);
            Backtrack(n, input, output, first + 1);
            input.Swap<int>(first, i);
            set.Add(input[i]);           
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


/*
 * @lc app=leetcode.cn id=215 lang=csharp
 *
 * [215] 数组中的第K个最大元素
 *
 * https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (58.39%)
 * Likes:    385
 * Dislikes: 0
 * Total Accepted:    85.6K
 * Total Submissions: 139.6K
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
 * 
 * 示例 1:
 * 
 * 输入: [3,2,1,5,6,4] 和 k = 2
 * 输出: 5
 * 
 * 
 * 示例 2:
 * 
 * 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
 * 输出: 4
 * 
 * 说明: 
 * 
 * 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
 * 
 */

// @lc code=start
public class Solution
{
    // public int FindKthLargest(int[] nums, int k) {
    //     var list = new List<int>();
    //     for(int i = 0; i < k; i++){
    //         list.Add(nums[i]);
    //     }
    //     list.Sort();
    //     for(int i = k; i < nums.Length; i++){
    //         if(nums[i] > list[0]){
    //             list.RemoveAt(0);
    //             int pos = BinarySearch(list, nums[i]);
    //             list.Insert(pos,nums[i]);
    //         }
    //     }
    //     return list[0];
    // }

    // //寻找第一个大于等于target的位置
    // private int BinarySearch(List<int> list, int target){
    //     int p = 0, q = list.Count();
    //     while(p < q) {
    //         int mid = (p + q) / 2;
    //         if(list[mid] < target)
    //             p = mid + 1;
    //         else
    //             q = mid;
    //     }
    //     return p;
    // }

    public int FindKthLargest(int[] nums, int k)
    {
        int[] minHeap = InitMinHeap(nums.Take(k).ToArray());
        for (int i = k; i < nums.Length; i++)
        {
            if(nums[i] > minHeap[0]){
                Pop(ref minHeap);
                Push(ref minHeap, k - 1, nums[i]);
            }
        }
        return minHeap[0];
    }

    private int[] InitMinHeap(int[] input)
    {
        int[] result = new int[input.Length];
        for (int i = 0; i < input.Length; i++)
        {
            Push(ref result, i, input[i]);
        }
        return result;
    }

    private void Push(ref int[] minHeap, int pos, int item){
        minHeap[pos] = item;
        while (pos > 0)
        {
            var root = (pos - 1) / 2;
            if(minHeap[root] > minHeap[pos]){
                var tmp = minHeap[root];
                minHeap[root] = minHeap[pos];
                minHeap[pos] = tmp;
            }
            pos = root;
        }
    }

    private void Pop(ref int[] minHeap){
        var last = minHeap.Length - 1;
        minHeap[0] = minHeap[last];
        minHeap[last] = int.MaxValue;
        int root = 0;
        while (root < last)
        {
            int left = root * 2 + 1;
            int right = root * 2 + 2;
            if(left >= last)
                break;
            var next = minHeap[left] < minHeap[right] ? left : right;
            if(minHeap[root] < minHeap[next])
                break;
            var tmp = minHeap[root];
            minHeap[root] = minHeap[next];
            minHeap[next] = tmp;
            root = next;
        }
    }
}
// @lc code=end


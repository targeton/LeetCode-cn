/*
 * @lc app=leetcode.cn id=264 lang=csharp
 *
 * [264] 丑数 II
 *
 * https://leetcode-cn.com/problems/ugly-number-ii/description/
 *
 * algorithms
 * Medium (47.60%)
 * Likes:    201
 * Dislikes: 0
 * Total Accepted:    15.2K
 * Total Submissions: 31.1K
 * Testcase Example:  '10'
 *
 * 编写一个程序，找出第 n 个丑数。
 * 
 * 丑数就是只包含质因数 2, 3, 5 的正整数。
 * 
 * 示例:
 * 
 * 输入: n = 10
 * 输出: 12
 * 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
 * 
 * 说明:  
 * 
 * 
 * 1 是丑数。
 * n 不超过1690。
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int NthUglyNumber(int n) {
        long num = 1;
        var twoQ = new Queue<long>();
        twoQ.Enqueue(2L);
        var threeQ = new Queue<long>();
        threeQ.Enqueue(3L);
        var fiveQ = new Queue<long>();
        fiveQ.Enqueue(5L);
        while(n-- > 1){
            if(twoQ.Peek() < threeQ.Peek()){
                if(twoQ.Peek() < fiveQ.Peek()){
                    num = twoQ.Dequeue();
                    twoQ.Enqueue(num * 2);
                    threeQ.Enqueue(num * 3);
                    fiveQ.Enqueue(num * 5);
                }else{
                    num = fiveQ.Dequeue();
                    fiveQ.Enqueue(num * 5);
                }
            }else{
                if(threeQ.Peek() < fiveQ.Peek()){
                    num = threeQ.Dequeue();
                    threeQ.Enqueue(num * 3);
                    fiveQ.Enqueue(num * 5);
                }else{
                    num = fiveQ.Dequeue();
                    fiveQ.Enqueue(num * 5);
                }
            }
        }
        return (int)num;
    }
}
// @lc code=end


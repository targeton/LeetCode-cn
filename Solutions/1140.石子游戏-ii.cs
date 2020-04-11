/*
 * @lc app=leetcode.cn id=1140 lang=csharp
 *
 * [1140] 石子游戏 II
 *
 * https://leetcode-cn.com/problems/stone-game-ii/description/
 *
 * algorithms
 * Medium (53.79%)
 * Likes:    5
 * Dislikes: 0
 * Total Accepted:    442
 * Total Submissions: 837
 * Testcase Example:  '[2,7,9,4,4]'
 *
 * 亚历克斯和李继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。
 * 
 * 亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。
 * 
 * 在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
 * 
 * 游戏一直持续到所有石子都被拿走。
 * 
 * 假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：piles = [2,7,9,4,4]
 * 输出：10
 * 解释：
 * 如果亚历克斯在开始时拿走一堆石子，李拿走两堆，接着亚历克斯也拿走两堆。在这种情况下，亚历克斯可以拿到 2 + 4 + 4 = 10 颗石子。 
 * 如果亚历克斯在开始时拿走两堆石子，那么李就可以拿走剩下全部三堆石子。在这种情况下，亚历克斯可以拿到 2 + 7 = 9 颗石子。
 * 所以我们返回更大的 10。 
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= piles.length <= 100
 * 1 <= piles[i] <= 10 ^ 4
 * 
 * 
 */
public class Solution {
    private int[] sum;
    private int[,] hash;
    public int StoneGameII(int[] piles) {
        if(piles == null || piles.Length == 0)
            return 0;
        int n = piles.Length;
        sum = new int[n];
        sum[n-1] = piles[n-1];
        for(int i = n-2; i >=0 ; i--){
            sum[i] = piles[i] + sum[i+1];
        }
        hash = new int[n,n];
        return helper(piles, 0, 1);
    }

    private int helper(int[] a, int i, int M){
        if(i == a.Length)
            return 0;
        if(2*M >= a.Length - i){
            return sum[i];
        }
        if(hash[i,M] != 0)
            return hash[i,M];
        int min = int.MaxValue;
        for(int x = 1; x <= 2*M; x++){
            min = System.Math.Min(min, helper(a, i+x, Math.Max(x,M)));            
        }
        hash[i,M] = sum[i]-min;
        return hash[i,M];
    }
}


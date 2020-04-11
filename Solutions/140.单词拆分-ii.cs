/*
 * @lc app=leetcode.cn id=140 lang=csharp
 *
 * [140] 单词拆分 II
 *
 * https://leetcode-cn.com/problems/word-break-ii/description/
 *
 * algorithms
 * Hard (37.52%)
 * Likes:    91
 * Dislikes: 0
 * Total Accepted:    8.8K
 * Total Submissions: 23.8K
 * Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
 *
 * 给定一个非空字符串 s 和一个包含非空单词列表的字典
 * wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
 * 
 * 说明：
 * 
 * 
 * 分隔时可以重复使用字典中的单词。
 * 你可以假设字典中没有重复的单词。
 * 
 * 
 * 示例 1：
 * 
 * 输入:
 * s = "catsanddog"
 * wordDict = ["cat", "cats", "and", "sand", "dog"]
 * 输出:
 * [
 * "cats and dog",
 * "cat sand dog"
 * ]
 * 
 * 
 * 示例 2：
 * 
 * 输入:
 * s = "pineapplepenapple"
 * wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
 * 输出:
 * [
 * "pine apple pen apple",
 * "pineapple pen apple",
 * "pine applepen apple"
 * ]
 * 解释: 注意你可以重复使用字典中的单词。
 * 
 * 
 * 示例 3：
 * 
 * 输入:
 * s = "catsandog"
 * wordDict = ["cats", "dog", "sand", "and", "cat"]
 * 输出:
 * []
 * 
 * 
 */

// @lc code=start
public class Solution {
    public IList<string> WordBreak(string s, IList<string> wordDict) {
        return DFS(s, wordDict, new Dictionary<string, List<string>>());
    }

    private IList<string> DFS(string input, IList<string> wordDict, Dictionary<string, List<string>> dic){
        if(dic.ContainsKey(input))
            return dic[input];
        var result = new List<string>();
        if(input == ""){
            result.Add("");
            return result;
        }
        foreach (var word in wordDict)
        {             
            if(input.StartsWith(word)){
                var tmp = DFS(input.Substring(word.Length), wordDict, dic);
                foreach(var t in tmp){
                    result.Add(t == "" ? word : word + " " + t);
                }
            }
        }
        dic.Add(input, result);
        return result;
    }
}
// @lc code=end


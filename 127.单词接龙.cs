/*
 * @lc app=leetcode.cn id=127 lang=csharp
 *
 * [127] 单词接龙
 *
 * https://leetcode-cn.com/problems/word-ladder/description/
 *
 * algorithms
 * Medium (36.74%)
 * Likes:    134
 * Dislikes: 0
 * Total Accepted:    10.9K
 * Total Submissions: 29.7K
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
 * 的最短转换序列的长度。转换需遵循如下规则：
 * 
 * 
 * 每次转换只能改变一个字母。
 * 转换过程中的中间单词必须是字典中的单词。
 * 
 * 
 * 说明:
 * 
 * 
 * 如果不存在这样的转换序列，返回 0。
 * 所有单词具有相同的长度。
 * 所有单词只由小写字母组成。
 * 字典中不存在重复的单词。
 * 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 * 
 * 输出: 5
 * 
 * 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * ⁠    返回它的长度 5。
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 * 
 * 输出: 0
 * 
 * 解释: endWord "cog" 不在字典中，所以无法进行转换。
 * 
 */
 using System.Collections.Generic;
public class Solution {
    public int LadderLength(string beginWord, string endWord, IList<string> wordList) {
        ISet<string> wordSet = new HashSet<string>(wordList);
        if(!wordSet.Contains(endWord))
            return 0;
        ISet<string> first = new HashSet<string>(){ beginWord };
        ISet<string> second = new HashSet<string>(){ endWord };
        int counter = 0;
        while(first.Any() && second.Any()){
            counter++;
            if(first.Count > second.Count){
                ISet<string> tmp = first;
                first = second;
                second = tmp;
            }
            ISet<string> helper = new HashSet<string>();
            foreach (var word in first)
            {
                char[] arr = word.ToCharArray();
                for (int i = 0; i < arr.Length; i++)
                {
                    char old = arr[i];
                    for(char c='a'; c<='z'; c++){
                        if(arr[i] == c)
                            continue;
                        arr[i] = c;
                        string next = new string(arr);
                        if(second.Contains(next))
                            return counter + 1;
                        if(wordSet.Contains(next)){
                            helper.Add(next);
                            wordSet.Remove(next);
                        }                        
                    }
                    arr[i] = old;
                }
            }
            first = helper;
        }
        return 0;
    }
}


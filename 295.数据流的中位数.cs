/*
 * @lc app=leetcode.cn id=295 lang=csharp
 *
 * [295] 数据流的中位数
 *
 * https://leetcode-cn.com/problems/find-median-from-data-stream/description/
 *
 * algorithms
 * Hard (38.89%)
 * Likes:    126
 * Dislikes: 0
 * Total Accepted:    11.4K
 * Total Submissions: 26.3K
 * Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
 *
 * 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
 * 
 * 例如，
 * 
 * [2,3,4] 的中位数是 3
 * 
 * [2,3] 的中位数是 (2 + 3) / 2 = 2.5
 * 
 * 设计一个支持以下两种操作的数据结构：
 * 
 * 
 * void addNum(int num) - 从数据流中添加一个整数到数据结构中。
 * double findMedian() - 返回目前所有元素的中位数。
 * 
 * 
 * 示例：
 * 
 * addNum(1)
 * addNum(2)
 * findMedian() -> 1.5
 * addNum(3) 
 * findMedian() -> 2
 * 
 * 进阶:
 * 
 * 
 * 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
 * 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
 * 
 * 
 */

// @lc code=start
public class MedianFinder {

    /** initialize your data structure here. */
    private List<int> _cache;
    
    public MedianFinder() {
        _cache = new List<int>();
    }
    
    public void AddNum(int num) {
        int pos = FindInsertIndex(_cache, num);
        _cache.Insert(pos, num);
    }
    
    public double FindMedian() {
        int len = _cache.Count();
        if(len % 2 == 1){
            return _cache[len / 2] * 1.0;
        }else{
            return _cache[len / 2 - 1] * 1.0 / 2.0 + _cache[len / 2] * 1.0 / 2.0;
        }
    }

    private int FindInsertIndex(List<int> data, int target){
        int p = 0, q = data.Count();
        while(p < q){
            int mid = (p + q) / 2;
            if(data[mid] < target)
                p = mid + 1;
            else
                q = mid;
        }
        return p;
    }
    
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.AddNum(num);
 * double param_2 = obj.FindMedian();
 */
// @lc code=end


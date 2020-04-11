/*
 * @lc app=leetcode.cn id=146 lang=csharp
 *
 * [146] LRU缓存机制
 *
 * https://leetcode-cn.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (46.34%)
 * Likes:    455
 * Dislikes: 0
 * Total Accepted:    40.6K
 * Total Submissions: 87.5K
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
 * 
 * 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
 * 写入数据 put(key, value) -
 * 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 * 
 * 进阶:
 * 
 * 你是否可以在 O(1) 时间复杂度内完成这两种操作？
 * 
 * 示例:
 * 
 * LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
 * 
 * cache.put(1, 1);
 * cache.put(2, 2);
 * cache.get(1);       // 返回  1
 * cache.put(3, 3);    // 该操作会使得密钥 2 作废
 * cache.get(2);       // 返回 -1 (未找到)
 * cache.put(4, 4);    // 该操作会使得密钥 1 作废
 * cache.get(1);       // 返回 -1 (未找到)
 * cache.get(3);       // 返回  3
 * cache.get(4);       // 返回  4
 * 
 * 
 */

// @lc code=start
public class LRUCache {
    private class Node {
        public int Key { get; set; }
        public int Val { get; set; }
        public Node Prev { get; set; }
        public Node Next { get; set; }
    }

    private Node head, tail;
    private Dictionary<int, Node> dic;
    private int _capacity;
    public LRUCache(int capacity) {
        dic = new Dictionary<int, Node>();
        head = new Node();
        tail = new Node();
        head.Next = tail;
        tail.Prev = head;
        _capacity = capacity;
    }
    
    public int Get(int key) {
        if (dic.ContainsKey(key)) {
            var node = dic[key];  
            MoveHead(node);          
            return node.Val;
        }
        return -1;
    }
    
    public void Put(int key, int value) {
        if (dic.ContainsKey(key)) {
            var node = dic[key];
            node.Val = value;
            MoveHead(node);
        } else {
            var n = new Node(){Key = key, Val = value};
            n.Prev = head;
            n.Next = head.Next;
            head.Next.Prev = n;
            head.Next = n;
            dic.Add(key, n);
            if(dic.Count() > _capacity) {
                n = tail.Prev;
                tail.Prev = tail.Prev.Prev;
                tail.Prev.Next = tail;    
                dic.Remove(n.Key);
                n.Prev = null;
                n.Next = null;        
            }
        }
    }

    private void MoveHead(Node n) {
        n.Prev.Next = n.Next;
        n.Next.Prev = n.Prev;
        n.Prev = head;
        n.Next = head.Next;
        head.Next.Prev = n;
        head.Next = n;
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end


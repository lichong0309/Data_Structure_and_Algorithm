'''
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
 

提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次

'''

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            index = ord(w) - ord('a')
            # 如果index的孩子节点暂时没有数据
            if cur.children[index] == None:
                newNode = Node()            # 创建新的节点
                cur.children[index] = newNode       # 向tree中添加新的节点
                cur = cur.children[index]           # 移动cur指针
            # 如果index的孩子节点已经存在数据
            else:
                cur = cur.children[index]
        cur.isEnd = True
 

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            index = ord(w) - ord('a')
            if cur.children[index] == None:
                return False
            else:
                cur = cur.children[index]
        if cur.isEnd == False:
            return False
        else:
            return True 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            index = ord(w) - ord('a')
            if cur.children[index] == None:
                return False
            else:
                cur = cur.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
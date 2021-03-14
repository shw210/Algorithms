## BFS Template
```Python
        queue = collections.deque([node])
        distance = {node ： 0}
        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor in distance:
                    continue
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
```

### 133. Clone Graph
思想：劝分不劝合。 把方程分开写成小方程，更不容易出错，也更容易debug  
steps: 1. 通过BFS从原图给定的点找到所有点 2. 复制所有的点 3.复制所有的边

```Python
def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
       
       
        # find all the nodes
        nodes = self.find_nodes_by_bfs(node)
        # copy all nodes 
        mapping = self.copy_all_nodes(nodes)
        # copy all edges
        self.copy_all_edges(nodes, mapping)
        return mapping[node]
        
    def find_nodes_by_bfs(self, node):
        visited = set([node])
        queue = collections.deque([node])
        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
            
        return list(visited)
        
    def copy_all_nodes(self, nodes):
        mapping = {}
        if not nodes: return
        for node in nodes:
            mapping[node] = Node(node.val)
        return mapping
    
    def copy_all_edges(self, nodes, mapping):
        if not nodes: return
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
            
```
### Lintcode 122. Word Ladder
主方程就是 BFS 的模板。注意 get_neibor_words 的时间复杂度为 O(52 * L^2) = O（L * 26 * 2L)
```Python
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = collections.deque([start])
        distance = {start: 1}

        while queue:
            word = queue.popleft() 
            for next_word in self.get_neibor_words(word, dict):
                if next_word in distance:
                    continue 
                if next_word == end:
                    return distance[word] + 1 
                distance[next_word] = distance[word] + 1 
                queue.append(next_word)

        return 0 

    def get_neibor_words(self, word, dict):
        neibor_words = []

        for i in range(len(word)): # 循环 L 次
            left, right = word[:i], word[i+1:] # 此处创建了新的字符串，时间复杂度为 O(L)，跟下面的 O(52L)相比比较小，可以忽略不计
            for character in "abcdefghijklmnopqrstuvwxyz": # 时间复杂度为 O（26）
                if word[i] == character:
                    continue
                neibor_word = left + character + right # 创建了新的字符串，时间复杂度为 O(L)
                if neibor_word in dict: # dictionary查找，时间复杂度为 O（L）
                    neibor_words.append(neibor_word)
        
        return neibor_words
```

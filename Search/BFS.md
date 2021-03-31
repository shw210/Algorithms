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

### 102. Binary Tree Level Order Traversal
注意分层遍历的方法
```Python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = collections.deque([root])
        result = [] 

        while queue:
          # 将当前层的所有点的值放到result里
          result.append([node.val for node in queue])
          # pop掉当前层，拓展出下一层的点放到queue里
          for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
        
        return result
```
## 连通块问题 
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
### Lintcode 433. Number of Islands
采用BFS寻找所有与 ‘1’ 相连的格子，这样算一个island。这道题如果采用 DFS 就会有stack overflow的问题
```Python
from collections import deque

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
                    
        return islands                    
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]
```

## 简单图最短路径
### Lintcode 122. Word Ladder
主方程就是 BFS 的模板。注意 get_neibor_words 的时间复杂度为 O(52 * L^2) = O（L * 26 * 2L)                  
Python 队列建议使用用 deque. Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
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

### Lintcode 611. Knight shortest path 
层级遍历问题，可以使用哈希表记录到所有点的距离。                
也可以多一重循环如下
```Python
        queue = collections.deque([node])
        distance = {node ： 0}
        while queue:
            for _ in range(len(queue)): # 多了这一层循环
                current_node = queue.popleft()
                for neighbor in current_node.neighbors:
                    if neighbor in distance:
                        continue
                        distance[neighbor] = distance[node] + 1
                        queue.append(neighbor)
```

题解，使用哈希表记录距离：
```Python
DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2)
]

class Solution:
        
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))
        return -1
        
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])

        if x < 0 or x >= n or y < 0 or y >= m:
            return False
            
        return not grid[x][y]
```

## 拓扑排序
算法描述:           
1. 统计每个点的入度             
2. 将每个入度为 0 的点放入队列(Queue)中作为起始节点                
3. 不断从队列中拿出一个点,去掉这个点的所有连边(指向其他点的边),其他点的相应的入度 - 1                
4. 一旦发现新的入度为 0 的点,丢回队列中

### Lintcode 127. Topological Sorting
         
```Python
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        indegree_dict = self.graph_to_indegree(graph) # 统计每个点的入度
        start_nodes = [node for node in indegree_dict if indegree_dict[node] == 0 ] #找出所有入度为零的点
        order = []
        queue = collections.deque(start_nodes) # 将入度为零的点放入 queue 中

        while queue:
            node = queue.popleft() # 去除入度为零的点
            order.append(node) # 并将入度为零的点放入最终的答案order中
            for neighbor in node.neighbors: # 将 这个入度为零的点的所有neighbor的入度减一
                indegree_dict[neighbor] -= 1
                if indegree_dict[neighbor] == 0: # 如果减一以后neighbor的入度变为零，则将其放入order中
                    queue.append(neighbor) 
        
        return order

    def graph_to_indegree(self, graph):
        indegree_dict = {node : 0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                indegree_dict[neighbor] += 1 

        return indegree_dict
```

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

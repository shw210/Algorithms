## BackTracking


### 257\. Binary Tree Paths (Easy)

```Python
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        results = []
        
        def helper(current, node):
            if node is None: 
                results.append(current)
                return
            
            if node.left is None and node.right is None:
                results.append(current + str(node.val))
            
            if node.left is not None:
                helper(current + str(node.val) + '->', node.left)
            
            if node.right is not None:
                helper(current + str(node.val) + '->', node.right)
            
        if not root: return []
        
        
        helper('', root)
        
        return results
```

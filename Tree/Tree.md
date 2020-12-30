## 110. Balanced Binary Tree
思路：先写一个function用于计算每个tree node的高度， 然后在 isBalanced function中，做两件事情：1. 判断当前root是否是balanced 2. 如果是的话，判断当前root的left node是否balance, 当前root的right node是否balance
```Python
class Solution(object):
    def isBalanced(self, root):
       
        if root is None: return True
        
        if abs(self.height(root.left) - self.height(root.right)) > 1: return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def height(self, node):
        if node is None: return -1
        
        return 1 + max(self.height(node.left), self.height(node.right))
```

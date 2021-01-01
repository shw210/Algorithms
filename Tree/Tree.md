## 110. Balanced Binary Tree
方法一思路：先写一个function用于计算每个tree node的高度。 然后在 isBalanced function中，做两件事情：1. 通过计算root左右child node的高度判断当前root是否是balanced 2. 如果是的话，判断当前root的left node是否balance, 当前root的right node是否balance。 因为计算node的高度时，都要把该Node下的所有Node都遍历一遍，一直到出现unbalanced node就会停止，所以时间复杂度是 nlog(n), 空间复杂度是o(n).
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
方法二的思路：先 keeping calling itself 一路走到底，从底层开始判断是否是balanced, 同时记录每一层的height (以用于判断panrent node是否是balanced). 每一次recursive call, 都是先走左边，走完了再走右边。这样保证每一个node只需要visit 一次，所以时间空间复杂度都是 O(n）。
```Python
class Solution(object):
    def isBalanced(self, root):
        return self.helper(root)[0]
        
    def helper(self, root):
        if not root: return True, -1
        
        left_balance, left_height = self.helper(root.left)
        
        if not left_balance: return False, 0
        
        right_balance, right_height = self.helper(root.right)
        
        if not right_balance: return False, 0
        
        height = 1 + max(left_height, right_height)
        
        return (abs(left_height - right_height) < 2), height
       
```
这两种方法的差别在tree为 [3,9,10,6,null,null,9,7,null,null,8] 时，很明显

## 112. Path Sum
思路： DFS. 注意test cases 要求当root 为null时，即使 sum = 0 也应该返回false. 所以写法改成了先判断 root是否为none, 往下走的时候没有走到 null node， 知道最下面一层node就判断返回值了。
```Python
class Solution(object):
    def hasPathSum(self, root, sum):
        
        if root is None: return False
        
        if not root.left and not root.right and sum == root.val: return True
        
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
    
  
```
## 437. Path Sum III

方法一思路: 对于每一个node，我会做两件事情。一是计算该node的presum并记录在dictionary里面; 二是check, check 该node的presum是否等于target, check 该node的presum 与 target的差值是否等于之前路径上的node的presum      
注意：因为 dictionary 是mutable的，所以我们到达左边最低端以后要 cache[presum] -= 1，否则被更改后的 cache就会被carry到右边node的dfs里。同时，我们的Presum没有这个问题，因为integer不是mutable的，所以即使当我对其加一时，我其实也是新建了一个identity，所以不会影响右边的node dfs
```Python
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        
        self.result = presum = 0
        cache = {}
        
        self.dfs(root, presum, sum, cache)
        
        return self.result
    
    def dfs(self, root, presum, target, cache):
        if not root: return
        
        presum += root.val
        
        if presum == target: 
            self.result += 1
        
        self.result += cache.get(presum - target, 0)
        
        cache[presum] = cache.get(presum, 0) + 1
        
        
        
        self.dfs(root.left, presum, target, cache)
        self.dfs(root.right, presum, target, cache)
        
        cache[presum] -= 1
```

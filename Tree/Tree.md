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

方法一思路: 对于每一个node，我会做两件事情。一是计算该node的presum并记录在dictionary里面; 二是check, check 该node的presum是否等于target, check 该node的presum 与 target的差值是否等于之前路径上的node的presum. 这种方法的时间空间复杂度都是 o(n）      
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
方法二：brute force。 从上到下一个一个作为root遍历, 只要路径上相等就 result += 1. 我们通过dfs function 来loop through tree, 通过test function 来检测当下该点作为root是多少条路径可取。
这种方法的时间复杂度是 o(n^2), 空间复杂度是 o(n).
```Python
class Solution(object):
    
    def pathSum(self, root, sum):
        
        self.result = 0
        
        self.dfs(root, sum)
        
        return self.result
        
    def dfs(self, root, target):
        if not root: return
        
        self.test(root, target)
            
        self.dfs(root.left, target)
        self.dfs(root.right, target)
        
    def test(self, root, target):
        if not root: return
        
        if root.val == target:
            self.result += 1
            
        self.test(root.left, target - root.val)
        self.test(root.right, target - root.val)
```
## 111. Minimum Depth of Binary Tree
思路：BFS. 记录cnts, 遇到左右都没有child的，就返回cnts
```Python
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        
        stack = [(root, 1)]
        
        while stack:
            curr, cnt = stack.pop(0)
            if not curr.left and not curr.right: return cnt
            if curr.left:
                stack.append((curr.left, cnt + 1))
            if curr.right:
                stack.append((curr.right, cnt + 1))
        
```
## 404. Sum of Left Leaves
思路一：BFS 
```Python
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        ttl, stack = 0, [root]
        
        while stack:
            curr = stack.pop(0)
            
            if curr.left and curr.left.left is None and curr.left.right is None:
                ttl += curr.left.val
                
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        return ttl
```
思路二：dfs     
注意：global variable 的用法
```Python
class Solution(object):
    def sumOfLeftLeaves(self, root):
        
        self.sum = 0
        
        self.dfs(root)
        
        return self.sum
        
    def dfs(self, root):
        
        if not root: return
        
        if root.left and not root.left.left and not root.left.right:
            self.sum += root.left.val
            
        self.dfs(root.left)
        self.dfs(root.right)
```


## 687. Longest Univalue Path
思路：在traverse(node)中，left_len 是必须经过 node.left 的最长 univalue path，left 是 必须经过node的最长左边的 univalue path, 同理 for the right side. 然后计算此刻必须经过 node 的unipath 最长 univalue path的长度 （即 left + right) , 并且 update 目前见过的 longest. 往上返值的时候只返回 max(left, right)， 因为时返回给 自己paranet node的 left_len/right_len, 所以只能选一边的路径          


所以整体思路就是：从上往下一直到最底层的node，在每一个node的地方，我算几件事情：1. 必须经过 自己的 left child node 的最长path，2. 必须经过自己的right child node的最长path 3. 必须经过自己的左右边的path 4. 将自己的longest path更新到 longest中 5. 将必须经过自己的左右最长path选一条返回给自己的parent node

```Python
class Solution(object):
    def longestUnivaluePath(self, root):
        
        # Time: O(n)
        # Space: O(n)
        longest = [0]
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        traverse(root)
        return longest[0]
```
## 337. House Robber III
思路：在每一个node都同时记录 在这个node上 偷或不偷 可达到的最大值，通过recursive call, 从下往上返值。        
note: 看到 tree，要想到用 recursive function, 从下往上返值
```Python
class Solution(object):
    def rob(self, root):
        ans = self.helper(root)
        return max(ans[0],ans[1])
    
    def helper(self, root):
        if not root: return [0, 0]
        
        res = [0, 0]
        
        left, right = self.helper(root.left), self.helper(root.right)
        
        res[0] = max(left[0], left[1]) + max(right[0], right[1]) # 不偷的话，随便child node 偷不偷，所以直接取最大值
        res[1] = root.val + left[0] + right[0] # 偷的话，只能取child node 不偷的最大值
        
        return res
    
```

## 671. Second Minimum Node In a Binary Tree

思路：往下遍历tree，如果遇到跟root value相同的点就继续travel, 如果遇到比root value更大的值但比 当前answer小的值就记录下来
```Python
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        self.ans = 2**31
        
        def helper(node):
            if not node: return
            
            if root.val < node.val < self.ans:
                self.ans = node.val 
                return
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        
        return -1 if self.ans == 2**31 else self.ans
```
另一种更高级的写法：
```Python
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1 
        
        def helper(node): #返回candidate
            if not node: return -1
        
            if node.val > root.val: return node.val  #只要比root.val大，就返回作为 candidate，并且不会继续往下visit，这点很关键
            
            #我们只会在有root.val的路径上追溯
            sl = helper(node.left) #若node.val = root.val, 则check其左右child
            sr = helper(node.right)
            
            if sl == -1: return sr # 自己的child只要有一个是空，则返回另外一个值 
            if sr == -1: return sl #只有当自己的两个child都是空，或者都等于root.val 才会返回 -1
        
            return min(sl, sr) #左右值一定都有效，否则在上一步就返回了
        
        
        return helper(root)
         
```
## 层次遍历

使用 BFS 进行层次遍历。通过 range(当前size），来控制层 , 因为在开始遍历一层的节点时，当前队列中的节点数就是当前层的节点数.

### 637. Average of Levels in Binary Tree
思路：BFS。 通过 range(当前size），来控制层并且 reset 当前sum         
注意：两个integer相除，必须用 a/float(b) 才能得到 float的答案。
```Python
class Solution(object):
    def averageOfLevels(self, root):
        
        if not root: return None
        
        result = []
        stack = [root]
        
        while stack:
            ttl = 0
            size = len(stack)
            
            for i in range(size):
                node = stack.pop(0)
                ttl += node.val
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            
            avg = ttl/float(size)
            result.append(avg)
            
        return result
```

### 513. Find Bottom Left Tree Value
思路：就是逐层遍历的思想，到了新的一层的时候第一个node就是最左边的node

```Python
class Solution(object):
    def findBottomLeftValue(self, root):
        row = [root]
        while row:
            first = row[0].val
            cnts = len(row)
            for i in range(cnts):
                node = row.pop(0)
                if node.left: row.append(node.left)
                if node.right: row.append(node.right)
                    
        return first
```

## 前中后序遍历

```html
    1
   / \
  2   3
 / \   \
4   5   6
```

- 层次遍历顺序：[1 2 3 4 5 6]
- 前序遍历顺序：[1 2 4 5 3 6]
- 中序遍历顺序：[4 2 5 1 3 6]
- 后序遍历顺序：[4 5 2 6 3 1]

层次遍历使用 BFS 实现，利用的就是 BFS 一层一层遍历的特性；而前序、中序、后序遍历利用了 DFS 实现。

前序、中序、后序遍只是在对节点访问的顺序有一点不同，其它都相同。

① 前序

```java
void dfs(TreeNode root) {
    visit(root);
    dfs(root.left);
    dfs(root.right);
}
```

② 中序

```java
void dfs(TreeNode root) {
    dfs(root.left);
    visit(root);
    dfs(root.right);
}
```

③ 后序

```java
void dfs(TreeNode root) {
    dfs(root.left);
    dfs(root.right);
    visit(root);
}
```
这类问题可参见“篮子王”讲解视频 ： https://www.youtube.com/watch?v=COBCEDPncus

### 144. Binary Tree Preorder Traversal
前序遍历
```Python
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        result = []

        def dfs(root, result):
            if not root: return 
            result.append(root.val)
            dfs(root.left, result)
            dfs(root.right, result)
        
        dfs(root, result)
        
        return result
```

### 145. Binary Tree Postorder Traversal 
后序遍历，跟144题相比只是调整了顺序
```Python
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return
        
        result = []
        
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
        
        dfs(root)
        
        return result
```

### 94. Binary Tree Inorder Traversal

```Python
class Solution(object):
    def inorderTraversal(self, root):
        
        ans = []
        
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
            
        dfs(root)
        
        return ans
```

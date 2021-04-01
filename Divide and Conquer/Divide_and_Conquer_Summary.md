## 模板

```Python
class Solution(object):
     def divideConquer(self, root):
          if not root:
               # 处理空树应该返回的结果
          
          if not root.left and not root.right:
          # 处理叶子节点应该返回的结果
          # 如果叶子的返回结果可以通过两个孔结点的返回结果得到，就可以省略这一段代码
          
          
          左子树返回结果 = divideConquere(root.left)
          右子树返回结果 = divideConquere(root.right)
          整棵树的结果 = 按照一定方法合并左右子树的结果
          
          return 整棵树的结果
     
```
## 遍历法 vs 分治法 257. Binary Tree Paths
### 遍历法
通过共享参数 result 到各个点去记录结果。      
注意：找点不需要手动回溯；求路径时，需要手动回溯。          
这种回溯的写法 优于 path + str(root.val) + '->' 的写法，因为加号会重新生成一个新的变量，复制一遍path，增加了时间复杂度
```Python
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if not root:
            return []
        
        result = []
        self.dfs(root, [str(root.val)], result)

        return result

    def dfs(self, root, current_path, result):
        if not root.left and not root.right:
            result.append('->'.join(current_path))
            return
        
        if root.left:
            current_path.append(str(root.left.val))
            self.dfs(root.left, current_path, result)
            current_path.pop() # 回溯
        
        # 也可以写成这样， 但是不推荐，因为当使用加号时，path + str(root.val) + '->' 会重新生成一个新的变量，复制一遍path，增加了时间复杂度
        #if root.left:
        #    self.helper(root.left, path + str(root.val) + '->', paths)
        


        if root.right:
            current_path.append(str(root.right.val))
            self.dfs(root.right, current_path, result)
            current_path.pop() # 回溯
```

### 分治法
通过 return value 记录子问题的结果
```Python
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        
        if not root.left and not root.right:
            paths = [str(root.val)]
            return paths
        
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)

        paths = []
        for path in left_paths + right_paths:
            paths.append(str(root.val) + '->' + path)

        return paths
```


### 53 Maximum Subarray

思路：divide and conquer
从中点，把nums分成left，right，和cross，相互比较求最大值为答案；不断分割至最短list，然后往上返回答案.
参考video：https://www.youtube.com/watch?v=OVvgiWeKI14  (3:05)
     
 ``` python
 class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        m = (0 + (len(nums) - 1)) // 2
        
        left_sum = self.maxSubArray(nums[:m+1])
        right_sum = self.maxSubArray(nums[m+1:])
        cross_sum = self.crossSum(nums)
        
        return max(left_sum, right_sum, cross_sum)
    
    def crossSum(self, nums):
        m = (0 + (len(nums) - 1)) // 2
        
        right, left = 0, 0
        max_right, max_left = -float('inf'), -float('inf')
        
        for num in nums[m+1:]:
            right = right + num
            max_right = max(max_right, right)
        
        for num in reversed(nums[:m+1]):
            left = left + num
            max_left = max(max_left, left)
            
        return max_left + max_right
  ```

### Lintcode 596. Minimum Subtree
1. 避免全球变量的写法，减少bug       
2. 参数或返回值，可以代替全球变量       
3. 在这道题中，每个 subtree 需要 keep track 三个值，min_sum, min_root, root_sum

```Python
def findSubtree(self, root):
        # write your code here
        min_sum, min_root, root_sum = self.helper(root)
        
        return min_root
    
    def helper(self, root):
        if not root:
            return sys.maxsize, None, 0 
            
        left_min_sum, left_min_root, left_root_sum = self.helper(root.left)
        right_min_sum, right_min_root, right_root_sum = self.helper(root.right)
        
        root_sum = left_root_sum + right_root_sum + root.val
        
        if left_min_sum == min(left_min_sum, right_min_sum, root_sum):
            return left_min_sum, left_min_root, root_sum 
        
        if right_min_sum == min(left_min_sum, right_min_sum, root_sum):
            return right_min_sum, right_min_root, root_sum 
        
        return root_sum, root, root_sum

```
### LintCode 474. Lowest Common Ancestor II (有父指针）
使用 HashSet 记录从 A 到根的所有点. 访问从 B 到根的所有点,第一个出现在 HashSet 中的就是
```Python
def lowestCommonAncestorII(self, root, A, B):
        # write your code here

        A_parent = set()
    
        curr = A 
        while curr:
            A_parent.add(curr)
            curr = curr.parent 
        
        curr = B 
        while curr:
            if curr in A_parent:
                return curr
            curr = curr.parent
            
        return None
```
### 236. Lowest Common Ancestor of a Binary Tree
有什么就return什么
```Python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #Edge/Condition
        if not root: return None
        if root == p or root == q: return root #遇到第一个值就会返回
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: return root #左右都有值，返回root
        if left: return left # 都在左边，left就是碰见的第一个值，即root
        if right: return right
```
### 1644. Lowest Common Ancestor of a Binary Tree II 
两个node不一定在tree里，所以需要添加两个output，记录node是否在tree里。         
这道题和236， 都是要尽可能在中间过程多记录信息，方便最后输入output
```Python
def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_exist, q_exist, ans = self.helper(root, p, q)
        
        if p_exist and q_exist: return ans
        
        return None
        
    def helper(self, root, p, q):
        
        if not root: 
            return False, False, None
        
        left_p_exist, left_q_exist, left_ans = self.helper(root.left, p, q)
        right_p_exist, right_q_exist, right_ans = self.helper(root.right, p, q) 
        
        p_exist = left_p_exist or right_p_exist or root == p
        q_exist = left_q_exist or right_q_exist or root == q
        
        if root == p or root == q:
            return p_exist, q_exist, root
        
        if left_ans and right_ans: return p_exist, q_exist, root
        if left_ans: return p_exist, q_exist, left_ans
        if right_ans: return p_exist, q_exist, right_ans
        
        return p_exist, q_exist, None  ### 记得写这行
```
### 114. Flatten Binary Tree to Linked List
helper function return the last node and modify
```Python
def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        
    def helper(self, root):
        """
        return last node and modify
        """ 
        if not root: return None 
        
        # root is last node 
        if not root.left and not root.right:
            return root 
        
        last_left = self.helper(root.left)
        last_right = self.helper(root.right)
        
        # connect
        if root.left:
            last_left.right = root.right
            root.right = root.left
            root.left = None
        
        return last_right or last_left #注意这种写法
        
```

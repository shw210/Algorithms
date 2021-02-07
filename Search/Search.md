# DFS
## DFS 组合类问题
### Lintcode 17. Subsets 
方法一：[1,2,3] 的树长下面这样 (这不是二叉树）。dfs 会先一路走到底，然后再回溯
```html 
                  [ ]               # result.append() 那行会把每个 node（即当先subset）先加到结果里，然后再 for loop里继续添加数字
        [1]       [2]       [3]     # for loop 会挨个处理后面可选的数字，但会先在[1]的subtree上一路走到底
    [1,2] [1,3] [2,3]
[1,2,3] 
```
需要注意的是 result.append(list(current_set)) 的写法，where 我们深度复制了 current set 并添加到最终结果中。如果写成 result.append(current_set)，我们添加的只是一个reference, 当 current_set 改变时，result也会随着改变。
```Python
def subsets(self, nums):
        # write your code here
        result = []
        self.dfs(sorted(nums), 0, [], result)
        return result
        
        
    def dfs(self, nums, startIndex, current_set, result):
        result.append(list(current_set))
        
        for i in range(startIndex, len(nums)):    # startIndex保证了我只会从后面的数字里选数，不会出现选了 [1,2] 然后又选了 [2,1]
            current_set.append(nums[i]) # [1] -> [1,2]
            self.dfs(nums, i + 1, current_set, result) # 寻找以 [1,2] 开头的所有子集
            current_set.pop()  #回溯 [1,2] -> [1]
    
```


方法二：在树的每一层上考虑加 nums[i] 还是不加, subset 只在最下面一层的叶子节点上。我们采用dfs，会先一路走到底      
```Python
def subsets(self, nums):
        result = []
        current_set = []
        index = 0
        
        self.dfs(sorted(nums), index, current_set, result)
        
        return result
        
    def dfs(self, nums, index, current_set, result):
        
        if index == len(nums):
            result.append(list(current_set))
            return
            
        current_set.append(nums[index]) # 加这个index上的number的情况
        self.dfs(nums, index + 1, current_set, result)
        current_set.pop() # 不加这个index的number 的情况
        self.dfs(nums, index + 1, current_set, result)
        
```

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

### 46. Permutations
```html
[1,1,2] have the following unique permutations:
[[1,1,2], [1,2,1], [2,1,1]]
```

思路：     
recursive function: loop through the nums, 轮流将i位的数字挑出来放到prefix里，剩下的字段属于备选. 将这个过程一直进行到剩下的字段为零为止，将prefix贴到answer里. 

```Python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        prefix = []
        
        def helper(prefix, sufix):
            if len(sufix) == 0:
                answer.append(prefix)
                
            for i in range(len(sufix)):
                helper(prefix + [sufix[i]], sufix[:i] + sufix[i + 1:]) 
                
        
        helper(prefix, nums)
        
        return answer
```
## 47. Permutations II      

思路：与46题相似，只不过有duplicates，所以当余下数字为【1，1，2】时，我真实的可选数字只有两个【1，2】。详情见leetcode上的答案

```Python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        prefix = []
        answer = []
        n = len(nums)
        
        
        def helper(prefix, sufix):
            if len(prefix) == n:
                answer.append(prefix)
                return
            
           
            #方法一：
            for num in set(sufix):
                i = sufix.index(num)
                helper(prefix + [sufix[i]], sufix[:i] + sufix[i + 1:]) 
            #方法二：
            #visited = set()
            #for i in range(len(sufix)):
               # if sufix[i] not in visited:
                  #  helper(prefix + [sufix[i]], sufix[:i] + sufix[i + 1:]) 
                  #  visited.add(sufix[i])
            
        helper(prefix, nums)
        
        return answer
```

## 77. Combinations 
```html
return all possible combinations of k numbers out of 1 ... n.
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```
思路：通过Prefix function 记录目前的答案，同时更新 helper function 的参数
```Python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        answer = []
        
        prefix = []
        
        def helper(prefix, n1, k1):
            if k1 < 0 or n1 < 0 or n1 < k1: return
            
            if k1 == 0: 
                answer.append(prefix)
                return
        
            for i in range(n1):
                helper(prefix + [n1 - i], n1 - i - 1, k1 - 1)
            
            
        helper(prefix, n, k)
        
        return answer
```

## 39. Combination Sum

从 candidates list中找到sum为target的数字组合
```html
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```
Solution:

```Python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        prefix = []
        answer = []
        
        def helper(prefix, sufix, target):
            if target < 0: return
            
            if target == 0:
                answer.append(prefix)
                return
            
            for i in range(len(sufix)):
                helper(prefix + [sufix[i]], sufix[i:], target - sufix[i])
                
                
        
        helper(prefix, candidates, target)
        
        return answer
```

## 90. Subsets II

与78类似，只不过有duplicate numbers in the sets, 记得要先sort

``` Python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        prefix = []
        
        def helper(prefix, sufix, k):
            if k == 0:
                answer.append(prefix)
                return
            
            #方法一：
            #for num in set(sufix):
            #    i = sufix.index(num)
            #    helper(prefix + [sufix[i]], sufix[i + 1:], k - 1) 
            
            #方法二：
            visited = set()
            
            for i in range(len(sufix)):
                if sufix[i] not in visited:
                    helper(prefix + [sufix[i]], sufix[i + 1:], k - 1)
                    visited.add(sufix[i])
        
        for k in range(len(nums) + 1):
            helper(prefix, nums.sort(), k)
            
            
        return answer



```
## 131. Palindrome Partitioning
注意：如何判断 s 是不是 palindrome， 可直接用 s == s[::-1] 的写法
```Python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        prefix = []
        answer = []
        
        
        def helper(prefix, sufix):
            if not sufix:
                answer.append(prefix)
                
            for i in range(len(sufix)):
                if sufix[:i + 1] == sufix[:i + 1][::-1]:
                    helper(prefix + [sufix[:i + 1]], sufix[i + 1:])
                    
        helper(prefix, s)
        
        
        return answer
```
## 37. Sudoku Solver 数独
思路：1. 先遍历一遍棋盘，记录下每行每列每个box已经有的数字        
     2. 然后开始采用dfs的方法往空格里填数字i。如果失败要记得将上一个填的数字i复原为空，然后继续循环尝试填入数字 i + 1
```Python
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for index in range(9)]
        cols = [set() for index in range(9)]
        boxes = [set() for index in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[r // 3 * 3 + c // 3].add(num)
                    
        def helper(r, c):
            if r == 9: return True
            if c == 8:
                next_r, next_c = r + 1, 0
            else:
                next_r, next_c = r, c + 1
                
            if board[r][c] != '.':
                return helper(next_r, next_c)
            
            for num in range(1, 10):
                if str(num) not in rows[r] and str(num) not in cols[c] and str(num) not in boxes[r // 3 * 3 + c // 3]:
                    board[r][c] = str(num)
                    rows[r].add(str(num))
                    cols[c].add(str(num))
                    boxes[r // 3 * 3 + c // 3].add(str(num))
                    if helper(next_r, next_c): return True
                    board[r][c] = "."
                    rows[r].remove(str(num))
                    cols[c].remove(str(num))
                    boxes[r // 3 * 3 + c // 3].remove(str(num))
             
            return False
            
            
            
    
        helper(0, 0)
```

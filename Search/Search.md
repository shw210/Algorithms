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

## 78. Subsets

找出所有子集
```html
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```
注意，如果nums = [1, 2, 3], 那么nums[3:] 为 [], 不会报错    

Solution:
```Python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # assume nums only contain distinct numbers
        prefix = []
        answer = []
        
        def helper(prefix, sufix, k):
            if k == 0:
                answer.append(prefix)
                return
            
            if len(sufix) == 0: return
            
            for i in range(len(sufix)):
                helper(prefix + [sufix[i]], sufix[i + 1:], k - 1) #注意，可以写sufix[i + 1:]，不会报错
            
        for i in range(len(nums) + 1):
            helper(prefix, nums, i)
            
            
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

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




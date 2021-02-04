
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

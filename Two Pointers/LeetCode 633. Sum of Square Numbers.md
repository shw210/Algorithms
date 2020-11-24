633. Sum of Square Numbers    

思路：双指针，注意范围可以缩小到 square root 往前

```Python
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        
        i, j = 0, int(sqrt(c))
        
        while i <= j:
            sqr_sum = i**2 + j**2 
            if sqr_sum == c:
                return True
            elif sqr_sum < c:
                i += 1
            else:
                j -= 1 
                
        return False
```

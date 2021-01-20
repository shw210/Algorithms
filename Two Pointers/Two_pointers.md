## 反转型题目
### 125. Valid Palindrome

注意：1. 访问下标的时候先检查没有越界  2. isalpha() 和 isdigit()

```Python
class Solution(object):
    def isPalindrome(self, s):
        
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.isValid(s[left]):
                left += 1
                
            while left < right and not self.isValid(s[right]):
                right -= 1
                
            while left < right and lower(s[left]) != lower(s[right]):
                return False
            
            left += 1
            right -= 1
            
        return True
    
    def isValid(self, letter):
        return letter.isalpha() or letter.isdigit()
```
## Two sums 型题目
### 1. Two Sum
方法一：dictionary， 时间空间复杂度都是o(n)
```Python
class Solution(object):
    def twoSum(self, nums, target):
        h = {}
        
        for i in range(len(nums)):
            if target - nums[i] in h:
                return [h[target-nums[i]],i]
            h[nums[i]]= i
```

方法二：two pointers，需要先排序          

注意 numbers = [(number, index) for index, number in enumerate(nums)] 的写法
```Python
class Solution(object):
    def twoSum(self, nums, target):
        
        if not nums: return [-1, -1]
        
        numbers = [
            (number, index) 
            for index, number in enumerate(nums)
        ]
        
        numbers.sort()
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            ttl = numbers[left][0] + numbers[right][0]
            if ttl > target: 
                right -= 1
            elif ttl < target: 
                left += 1
            else:
                return [numbers[left][1], numbers[right][1]]
            
```




















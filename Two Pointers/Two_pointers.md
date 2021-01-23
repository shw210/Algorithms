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
### 170. Two Sum III - Data structure design
方法一： hash table. AddNumber - O(1). FindTwoSum - O(n)

```Python
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}  # 注意对initiation function的理解
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.count:
            if value - num in self.count and (value - num != num or self.count[num] > 1):
                return True
        
        return False
        
```


## Partition 型题目 （排序）

### 75. Sort Colors
思路: 'left' tracks where 0 goes next; 'right' tracks where 2 goes next; 'i' travel through the list        
we need to make sure all the numbers before 'left' is zeros, and all the numbers between 'right' and 'i' are 1s, and all the numbers after 'right' are 2s. that's why when we switch 'right' and i, we need to check what i is again and thus don't do i+=1; but when we switch 'left' and i, we don't need to check what i is and do i+=1. Note that we need to do while loop till i <= right, to make sure that i travel through the whole list

```Python
class Solution(object):
    def sortColors(self, nums):
       
        left, i, right = 0, 0, len(nums) - 1
        
        while i <= right:
            
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
                
                
```


















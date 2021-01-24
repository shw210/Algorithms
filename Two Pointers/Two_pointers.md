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
方法二： Two pointers. 
##### AddNumber - O(n)      
##### FindTwoSum - O(n)     
其中 AddNumber 可以使用 Insertion Sort 的方法. 先将数加到数组的末尾,然后一直往前交换到它的所在位置
```Python
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.numbers.append(number)
        i = len(self.numbers)  - 1
        while i >= 1 and self.numbers[i] < self.numbers[i - 1]:
            self.numbers[i], self.numbers[i - 1] = self.numbers[i - 1], self.numbers[i]
            i -= 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if not self.numbers: return False
        
        left, right = 0, len(self.numbers) - 1 
        while left < right:
            ttl = self.numbers[left] + self.numbers[right]
            if ttl == value: return True
            if ttl < value:
                left += 1
            elif ttl > value:
                right -= 1
        
        return False
```

### 15. 3Sum

思路：先排序。 假设 a <= b <= c。for 循环 a ，找 b + c = -a 即可调用 two sum 的算法来解决。这样就通过降维，降时间复杂度降到了O(n^2).

如果处理duplicate numbers呢？通过记录上一个数字，或者上一个pair of numbers

```Python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2: return []
        
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            self.twoSum(-nums[i], nums, i + 1, len(nums) - 1, result)
        
        return result
    
    def twoSum(self, target, nums, left, right, result):
        
        last_pair = None
        while left < right:
            ttl = nums[left]  + nums[right]
            if ttl == target and (nums[left], nums[right]) != last_pair:
                result.append([-target, nums[left], nums[right]])
                last_pair = (nums[left], nums[right])
            
            elif ttl > target:
                right -= 1
            else:
                left += 1
        
        return result
```

### 611. Valid Triangle Number 
思路：使用双指针算法。 for 循环最大边的位置 i，接下来的任务就是在 0~i-1 之间找到两数之和 > Si        

Note: 求具体方案 VS. 求方案个数。 求具体方案只能一个个数出来,时间复杂度 O(n^3). 求不可以重复的方案数也只能一个个数. 求可以重复的方案数可以批量累加,时间复杂度 O(n^2)
```Python
class Solution(object):
    def triangleNumber(self, nums):
       
        if len(nums) <= 2: return 0
        nums.sort()
        
        cnt = 0
        for i in range(len(nums)):
            
            left, right = 0, i - 1
            while left < right:
                ttl = nums[left] + nums[right]
                if ttl > nums[i]:
                    cnt += right - left 
                    right -= 1
                else:
                    left += 1
        
        return cnt
```

### 18. 4Sum
for a, b 的位置，c和d用 two sum 的双指针解法        
一一原创写法：
```Python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) <= 3: return []
        
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums)):
                if j >= i + 2 and nums[j] == nums[j - 1]: continue
                self.twoSum([nums[i], nums[j]], target, nums, j + 1, len(nums) - 1, result)
                
        return result
        
        
        
    def twoSum(self, pre_pairs, target, nums, left, right, result):
        last_pair = None
        while left < right:
            ttl = nums[left] + nums[right]
            want = target - pre_pairs[0] - pre_pairs[1]
            if ttl == want and (nums[left], nums[right]) != last_pair:
                result.append(pre_pairs + [nums[left], nums[right]])
                last_pair = (nums[left], nums[right])
                left = left + 1
                right = right - 1
            elif ttl > want:
                right = right - 1
            else:
                left = left + 1 
```
两个模版答案：

```Python
class Solution(object):
    '''
    题意：找到数列中所有和等于目标数的四元组，需去重
    多枚举一个数后，参照3Sum的做法，O(N^3)    
    '''
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res
```

```Python
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        if not numbers:
            return []
            
        nums = sorted(numbers)
        results = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                pairs = self.find_two_sum_pairs(
                    nums,
                    j + 1,
                    len(nums) - 1,
                    target - nums[i] - nums[j],
                )
                
                for (c, d) in pairs:
                    results.append([nums[i], nums[j], c, d])
                
        return results
        
    def find_two_sum_pairs(self, nums, left, right, target):
        pairs = []
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                if not pairs or (nums[left], nums[right]) != pairs[-1]:
                    pairs.append((nums[left], nums[right]))
                left += 1
                right -= 1
        return pairs
```

### 454. 4Sum II
时间复杂度和空间复杂度均为 O(N^2). 将 a,b 组成的和及其组成方案个数统计在hash里，然后再去枚举 c,d 的组合，然后找 -(c+d) 在 hash 里的组合数。

```Python
def fourSumCount(self, A, B, C, D):
        counter = {}
        for a in A:
            for b in B:
                counter[a + b] = counter.get(a + b, 0) + 1
        answer = 0
        for c in C:
            for d in D:
                answer += counter.get(-c - d, 0)
        return answer
```

## Partition 型题目 （排序）

### Lintcode 31. Partition Array

Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:      

All elements < k are moved to the left      
All elements >= k are moved to the right        
Return the partitioning index, i.e the first index i nums[i] >= k.      

思路一：     
通过头尾指针跳过小于k的前缀和大于等于k的后缀，可以找到与第一个大于等于k的值和最后一个小于k的值。进行交换后可达到划分数组的目的，直到找到两个指针相遇为止。

伪代码如下：

令left = 0，right = length-1。     
当nums[left] < k时，left指针向右移动。        
当nums[right] >= k时，right指针向左移动。     
如果left <= right，交换两个值。      
如果left > right，返回left作为最终结果，否则返回第二步。

```Python
def partitionArray(self, nums, k):
        # write your code here
        left, right = 0, len(nums) - 1 
        
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1 
            
            while left <= right and nums[right] >= k:
                right -= 1 
            
            if left <= right:  #注意一定要有这个条件 
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1  
                right -= 1 
            
        
        return left 
```
另外，需要注意一下 partition array 和 quick sort 里面的partition 的区别 (> k 不是 >= k)，quick sort 里的partition 的写法如下：
``` Python 
def partition(self, nums, k):
        # write your code here
        left, right = 0, len(nums) - 1 
        
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1 
            
            while left <= right and nums[right] > k: # 注意是 > k 不是 >= k，这种差别就是为了保证 partiton funciton 能够将数字尽量平均的分配在k两边，拿个例子【1，1，1，1，1，11】, k = 1 过一遍就清楚了
                right -= 1 
            
            if left <= right:  #注意一定要有这个条件 
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1  
                right -= 1 
            
        
        return left 

```




partition array 思路二 但这种方法交换数字的次数可能过多
```Python
def partitionArray(self, nums, k):
        # write your code here
        next_small_index = 0
        
        for i in range(len(nums)):
            if nums[i] < k:
                nums[i], nums[next_small_index] = nums[next_small_index], nums[i]
                next_small_index += 1 
        
        return next_small_index
```



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

        
















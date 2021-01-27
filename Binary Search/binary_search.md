# 介绍
## 方法一 Implementation
```Python
L = 0, R = N - 1

ans = -1

while L <= R:
	mid = L + (R - L) // 2
	if a[mid] >= target:
		ans = mid
		R = mid - 1
	else:
		L = mid + 1
		
return ans
```


problems suited for binary search: sorted array, looking for some target that satisfied some conditions

General idea: 
0. initialize the answer 
1. go to middle point, if middle point satisfies that condition, record that answer
2. decide which side to go next to find a better answer, if find a better one update the answer
3. loop until go through all the needed scan, ie. L > R

## 方法二implementation
```Python
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环, 比如
        # 样例：nums=[1，1] target = 1，这时如果进入while loop, mid = 0, start 也还是0， 寻找区间没有移动，就会出现死循环，
        # 为了统一模板，我们就都采用 start + 1 < end，就保证不会出现死循环
        while start + 1 < end:
            # python 没有 overflow 的问题，直接 // 2 就可以了
            mid = (start + end) // 2

            # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里，偷懒写法，不容易出错
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else: 
                end = mid

        # 因为上面的循环退出条件是 start + 1 < end
        # 因此这里循环结束的时候，start 和 end 的关系是相邻关系（1和2，3和4这种）
        # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1
```
在二分问题中，最常见的错误就是死循环。而这个模版一定不会出现死循环。为什么呢？
因为我们这边使用了start + 1 < end, 而不是start < end 或者 start <= end		
二分法的模板中，整个程序架构分为两个部分：		
通过 while 循环，将区间范围从 n 缩小到 2 （只有 start 和 end 两个点）。		
在 start 和 end 中判断是否有解。		
而普通的start < end 或者 start <= end 在寻找目标最后一次出现的位置的时候，可能出现死循环。

# 题目
### leetcode 34. Find First and Last Position of Element in Sorted Array
我们只介绍怎么 find last position of element in sorted array, first position 同理		

写法一：
```Python
def lastPosition(self, nums, target):
        # write your code here
        if not nums: return -1
        
        start, end = 0, len(nums) - 1 
        
        ans = -1
        
        while start <= end:
            
            mid = (start + end) // 2
            
            if nums[mid] == target:
                ans = mid
                start = mid + 1 
            elif nums[mid] > target:
                end = mid - 1 
            else: # nums[mid] < target
                start = mid + 1 
                
        return ans 
```

写法二：
```Python
class Solution:
    
    def lastPosition(self, nums, target):
        # write your code here
        
        if not nums: return -1
        
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else: #nums[mid] < target
                start = mid
            
        if nums[end] == target: return end 
        if nums[start] == target: return start
        return -1
```
### Lintcode 585. Maximum Number in Mountain Sequence

写法二：
```Python
def mountainSequence(self, nums):
        # write your code here
        # 思路：找到第一个比后面的数字大的number
        
	if not nums: return -1
	
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else: 
                start = mid 
                
        
        return max(nums[start], nums[end])
```
### LintCode 447. Search in a Sorted Array of Unknown Size
二分查找第一个不小于target的元素很简单. 但是需要确定二分区间的范围. 此时还是需要倍增地找到右边界.		

初始右边界为1, 如果右边界的数小于 target, 就将其倍增, 直到右边界不小于target.		

这时就可以二分查找了.		

注意: 越界访问是没有关系的, 因为这个ArrayReader在越界访问时, 返回 INT_MAX, 一定不小于 target. 而即使是返回 -1 之类的数值, 我们也可以加一个判断搞定.	

```Python
def searchBigSortedArray(self, reader, target):
        # write your code here
        start, end = 0, 1 
	
	# 怎么处理target在最后一个区间里呢？即出界前没找到 比target大的数字。
        # 答：没有关系，我最后一个end也算是找到了一个边界，(0 + end) //2 也一定在边界以内
        while reader.get(end) < target:
            end = end * 2 
            
        while start + 1 < end:
            mid = (start + end) // 2
            
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) > target:
                end = mid
            else:
                start = mid
                
        if reader.get(start) == target: return start
        if reader.get(end) == target: return end
        
        return -1
```

### 658. Find K Closest Elements
采用的是二分法 + 双指针 二分法确定一个位置，左侧是 < target，右侧是 >= target 然后用两根指针从中间向两边走，依次找到最接近的 k 个数. 注意：写了一个 leftIsCloser 的函数，将复杂的判断条件外包了出去，这样更不容易出错也更清晰。
```Python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        right = self.findFirstIndex(arr, x)
        left = right - 1 
        
        for _ in range(k):
            if self.leftIsCloser(arr, left, right, x):
                left -= 1 
            else:
                right += 1 
            
        return arr[left+1:right]
        
        
    def leftIsCloser(self, arr, left, right, target):
        if left < 0:
            return False
        if right >= len(arr):
            return True
        return target - arr[left] <= arr[right] - target
    
    
    
    def findFirstIndex(self, arr, x):    
        # binary search
        start, end = 0, len(arr) - 1 
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if arr[mid] >= x:
                end = mid
            elif arr[mid] < x:
                start = mid 
        
        if arr[start] >= x: return start
        if arr[end] >= x: return end
        
        return len(arr)
        
```
### 153. Find Minimum in Rotated Sorted Array
注意：采用将数字图像化的方法找规律


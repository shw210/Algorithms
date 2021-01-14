### 217. Contains Duplicate

```Python
class Solution(object):
    def containsDuplicate(self, nums):
        dic = set()
        
        for num in nums:
            if num not in dic: 
                dic.add(num)
            else:
                return True
            
        return False
```
### 594. Longest Harmonious Subsequence
思路：记录每个数字出现的次数，然后找相差为一的数的最大的次数和
```Python
from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = Counter(nums)
        max_cnt = 0
        
        for num in dic:
            if num + 1 in dic:
                max_cnt = max(max_cnt, dic[num + 1] + dic[num])
                
        return max_cnt
```
### 128. Longest Consecutive Sequence
方法一思路：只需要记录边界上的点的长度     
注意：因为碰到重复的数字我会直接过，所以处理一个新的数字时，它的left和right一定是目前的boundary number，所以left number对应的一定是左边的正确的length，right number对应的一定是右边的正确的length，因为我从一开始就确保boundary number所对应的length是正确的了。
```Python
class Solution(object):
    def longestConsecutive(self, nums):
        
        dic = {}
        max_len = 0
        for num in nums:
            if num in dic: continue
            
            total_len = 1
            left = num - 1
            right = num + 1
            if left in dic:
                left_len = dic[left]
                left_end = num - left_len
                total_len = total_len + left_len
                
            if right in dic:
                right_len = dic[right]
                right_end = num + right_len
                total_len = total_len + right_len
            
            if left in dic:
                dic[left_end] = total_len
            if right in dic:
                dic[right_end] = total_len
                
            dic[num] = total_len
            
            max_len = max(max_len, total_len)
            
        return max_len
                
```
方法二思路：用set来做。在set中寻找各个数段的最左边界, 即（num - 1) 不在set里的num，然后向右遍历计算长度
```Python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        max_cnt = 0
        
        for num in set_nums:
            cnt = 1
            
            if num - 1 not in set_nums:
                while num + 1 in set_nums:
                    cnt += 1
                    num += 1
                
            max_cnt = max(max_cnt, cnt)
            
        return max_cnt
```

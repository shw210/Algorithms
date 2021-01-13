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

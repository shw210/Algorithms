### 242. Valid Anagram
思路：dictionary
写法一：利用collections.Counter()将list转变成dictionary
```Python
class Solution(object):
    def isAnagram(self, s, t):
       
        return collections.Counter(s) == collections.Counter(t)
```

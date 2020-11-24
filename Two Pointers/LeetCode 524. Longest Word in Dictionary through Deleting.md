
524. Longest Word in Dictionary through Deleting  
思路：一个词一个词轮流查，查的时候用双指针
```python
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        n = len(s) - 1
        
        def findWord(word):
            m = len(word) - 1
            
            i, j = 0, 0
            
            while i <= n and j <= m:
                if s[i] == word[j]:
                    j += 1
                    if j == m + 1: return True
                i += 1
                
            return False
        
        longest = 0
        answer = ''
        
        for word in d:
            if findWord(word) and len(word) > longest:
                longest = len(word)
                answer = word
            
        return answer
```

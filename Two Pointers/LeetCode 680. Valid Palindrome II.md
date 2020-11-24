680. Valid Palindrome II  
巧思：通过写一个 sub function，可以往加入更多参数. 这种方法经常在recursive function 里面用到
```Python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        
        def palindrom(i, j):
            
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                    
                else:
                    if cnts == 1: return False
                    return palindrom(i + 1, j, cnts + 1) or palindrom(i, j - 1, cnts + 1)
                
            return True
                    
        return palindrom(0, len(s) - 1, 0)
```

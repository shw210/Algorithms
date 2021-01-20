## 九章算法

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

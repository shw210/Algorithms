345. Reverse Vowels of a String     

思路：双指针两边寻找
```Python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s)-1
        vowels = set(list("aeiouAEIOU"))       #set只take 一个input, 所以必须先写成list
        s = list(s)           # string不能index （例如如果 s = 'a'，就不能写s[0]), 所以必须先转成list
        
        while i <= j:
            left = s[i]
            right = s[j]
            if left in vowels and right in vowels:         # 想好有几种情况写if else, 在每种情况下index如何改变
                s[i], s[j] = right, left
                i += 1
                j -= 1
            else:
                if left not in vowels:
                    i += 1
                if right not in vowels: 
                    j -= 1
                
        return ''.join(s)         # ' '.join的写法哟！
```

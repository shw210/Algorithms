## 204. Count Primes

找出所有小于n的质数    

思路：从2开始，乘以比它大小于n的数字，将得出的数字花掉    
      然后是3    
      4 已经被划掉了，然后是5.    
      一直进行到sqrt(n)    
```Python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # define a boolean
        ans = [True] * n
        ans[:2] = [False] * 2
        
        for base in range(2, int(sqrt(n)) + 1):
            if ans[base]:
                for num in range(base * base, n, base):
                        ans[num] = False
        
        return sum(ans)
```
## 504. Base 7 
将数字转换成7进制，100 = 1 * 10^2 + 0 * 10^1 + 0 * 10^0, 用7进制表示就是 100 = 2 * 7^2 + 0 * 7^1 + 2* 7^0, 所以是'202'. 

```Python
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        neg = (num < 0)
        num = abs(num)
        
        ans = ''
        
        
        while num > 0:
            ans = str(num % 7) + ans
            num = num // 7 
        
        if neg:
            ans = '-' + ans
            
        return ans
```

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

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
## 172. Factorial Trailing Zeroes
思路：找10 -> 找 2* 5 -> 找 5. 所以有几个5，最后就有几个零           
10就是5的两倍，换句话说找到5了就一定能找到2，因为这是一个阶乘运算，好比5前面一定有2，15前一定有12.     
但是还有像25 = 5 *5 这样的数字，所以要一直除至 n = 0
```Python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        
        while n > 0:
            ans += n //5
            n = n // 5
            
        return ans
```
## 67. Add Binary （二进制相加）
思路：从后往前加，用carry记录进位。只要用一个index loop就行了，如果超过了string 的长度，可以根据条件跳过不加

```Python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        answer =''
        
        for i in range(max(len(a),len(b))):
            added = carry
            if i < len(a):
                added += int(a[-i - 1])
            if i < len(b):
                added += int(b[-i - 1])
            
            carry = added // 2
            added = added % 2
            
            answer += str(added)
         
        if carry:
            answer += str(carry)
        
        return answer[::-1]
            
```
## 415. Add Strings
注意 carry 和 temp_sum 的算法
```Python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        carry = 0
        answer = ''
        
        for i in range(max(n1, n2)):
            temp_sum = carry
            if i < n1:
                temp_sum += int(num1[-i - 1])
                
            if i < n2:
                temp_sum += int(num2[-i - 1])
                
            carry = temp_sum // 10
            temp_sum = temp_sum % 10
            
            answer = str(temp_sum) + answer
            
        if carry:
            answer = '1' + answer
            
        return answer
```
## 462. Minimum Moves to Equal Array Elements II
找中位数，比如 [1, 2, 3, 4, 5]. 如果从 3 换成 2， 则 前面只有两个数字movement减一，而后面有三个数字movement加一，所以 2 会比 3 差
```Python
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        mid = len(nums) // 2
        ans = 0
        
        for num in nums:
            ans += abs(num - nums[mid])
            
        return ans
```
## 169. Majority Element

``` Python
from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        mid = len(nums) // 2 + 1
        
        for num in nums:
            dic[num] += 1
            if dic[num] >= mid:
                return num
```

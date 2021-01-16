### 242. Valid Anagram

写法一：利用collections.Counter()将list转变成dictionary
```Python
class Solution(object):
    def isAnagram(self, s, t):
       
        return collections.Counter(s) == collections.Counter(t)
```
写法二：思路：建立一个长度为26的list，每个位置对应一个字母，记录其出现的次数。处理s的时候往上加次数，处理t的时候减次数，最后再看list里是否有不为零的，有就返回false。也可以用collections.defaultdict(int) 来初始化一个dictionary
```Python
class Solution(object):
    def isAnagram(self, s, t):
        cnts = [0] * 26
        
        for letter in s:
            cnts[ord(letter) - ord('a')] += 1
            
        for letter in t:
            cnts[ord(letter) - ord('a')] -= 1
            
        for cnt in cnts:
            if cnt != 0: return False
            
        return True
```
注意 cnts[ord(letter) - ord('a')] 的写法

### 409. Longest Palindrome
用collections.counter()来统计每个字母出现次数
```Python
class Solution(object):
    def longestPalindrome(self, s):
        
        dic = collections.Counter(s)
        result = 0
        single = 0
        
        for letter in dic:
            result += dic[letter] // 2 * 2  # 注意这个写法
        
        if result < len(s): result += 1  # 这个条件下 s 中一定有单个未使用的字符存在，可以把这个字符放到回文的最中间
            
        return result

```

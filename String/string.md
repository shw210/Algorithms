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
### 205. Isomorphic Strings
思路一：写两个dictionary，确保是一对一的关系                                                                                                                                     注意：如果有两个类似的段落，考虑用一个function更加简洁。                          
```Python
class Solution(object):
    def isIsomorphic(self, s, t):
        return self.helper(s, t) and self.helper(t, s)
    
    def helper(self, s, t):
        dic_s = {}
        l = len(s)
        
        for i in range(l):
            if s[i] not in dic_s:
                dic_s[s[i]] = t[i]
            elif dic_s[s[i]] != t[i]:
                return False        
        return True
```
思路二：记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构。
注意记录位置时要用 i + 1, 因为d1，d2的默认值为零，而上一个位置可能是零，所以不能用 i。      
注意 ord function 的用法

```Python
class Solution(object):
    def isIsomorphic(self, s, t):
        
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i + 1
            d2[ord(t[i])] = i + 1
            
        return True
```
### 647. Palindromic Substrings
思路：遍历各个character和间隙作为panlindoromes的center，从center开始向两边展开查看其是否是panlindromes.

```Python
class Solution(object):
    def countSubstrings(self, s):
        
        cnts = 0
        
        for i in range(2 * len(s) - 1):
            left = i // 2
            right = i // 2 + i % 2
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                cnts += 1
                left -= 1
                right += 1
            
        return cnts
```

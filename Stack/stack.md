## 394. Decode String
思路：维护两个stack，number_stack 记录重复次数，string_stack记录 number_stack里同一行的数字前面的string是什么，current记录刚刚入库的number所对应的string.     
loop through s, 当遇到 ']' 时开始解码, meaning 该乘乘该加加。note 数字的处理，如何进行进位的计算
```Python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        current = ''
        number_stack = []
        string_stack = []
        number = 0
        for i in range(len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            elif s[i] == '[':
                number_stack.append(number)
                number = 0
                string_stack.append(current)
                current = ''
            elif s[i].isalpha():
                current = current + s[i]
            elif s[i] == ']':
                current = number_stack.pop() * current
                current = string_stack.pop() + current
            
        return current
                
```
## 496. Next Greater Element I

思路：难点就是如何过一遍nums2，建立一个dictionary记录每个element的下一个最大值是什么。解决的方法就是 栈。在过list的时候，当前数字比栈的最后一个数字大，就stack.pop()并map进dictionary里;当前数字比栈的最后一个数字小，就将当前数字append to stack 

```Python
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        dic = {}
        res = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)
              
        while stack:
            for num in stack:
                dic[stack.pop()] = -1
                
        for num in nums1:
            res.append(dic[num])
            
        return res
```

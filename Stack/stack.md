## 394. Decode String
思路：维护两个stack，number_stack 记录重复次数，string_stack记录 number_stack里同一行的数字前面的string是什么，current记录刚刚入库的number所对应的string.     
loop through s, 当遇到 ']'时开始解码, meaning 该乘乘该加加
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

17\. Letter Combinations of a Phone Number(Medium)

方法一：写 recursive function, 在这个function中，current+letter 一步一步深入往上加letter，够长度了之后再加到answer里，这是dfs的思路


```Python
class Solution(object):
    def letterCombinations(self, digits):
       answer = []
       if not digits: return answer
        mapping = [0,1,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        def letterCombinationRecursive(answer,index, current):
            if index == len(digits):
                answer.append(current)
                return
            
            for letter in mapping[int(digits[index])]:
                letterCombinationRecursive(answer, index + 1, current + letter)
            
        letterCombinationRecursive(answer, 0, '')
        
        return answer 
```

方法二：loop，temp 存储轮到下一个数字时的中间答案，answer存储该数字结束时当前的所有答案。所以就是当前所有答案和下一个数字的letter的所有组合。感觉还是方法一比较容易bug free
```Python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits: return []
        
        answer = [""]
        
        mapping = [0, 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        for digit in digits:
            temp = []
            for letter in mapping[int(digit)]:
                for string in answer:
                    temp.append(string + letter)
                
            answer = temp
                
        return answer
```

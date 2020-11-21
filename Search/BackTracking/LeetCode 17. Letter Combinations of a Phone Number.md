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
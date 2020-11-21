思路: DFS  
写dfs function: 先判断base case， 然后写false的情况，过了之后往周边写 recursive dfs          
大function的思路就是循环每一个格子，如果跟word的第一个字母相等就 在这个格子上 call dfs function

``` Python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, indx):
            if indx == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[indx]:
                return False
            
            temp = board[i][j]
            board[i][j] = ' '
            
            have = dfs(i + 1, j, indx + 1) or dfs(i - 1, j, indx + 1) or dfs(i, j + 1, indx + 1) or dfs(i, j - 1, indx + 1)
            
            board[i][j] = temp
            return have 
        
        if not board or not board[0]: return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
                    
                
        return False      
                
```                
        

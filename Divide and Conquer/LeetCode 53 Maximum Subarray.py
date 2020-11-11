#LeetCode 53

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：divide and conquer
        
        从中点，把nums分成left，right，和cross，相互比较求最大值为答案；不断分割至最短list，然后往上返回答案
        
        参考video：https://www.youtube.com/watch?v=OVvgiWeKI14  (3:05)
        """
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        m = (0 + (len(nums) - 1)) // 2
        
        left_sum = self.maxSubArray(nums[:m+1])
        right_sum = self.maxSubArray(nums[m+1:])
        cross_sum = self.crossSum(nums)
        
        return max(left_sum, right_sum, cross_sum)
    
    def crossSum(self, nums):
        m = (0 + (len(nums) - 1)) // 2
        
        right, left = 0, 0
        max_right, max_left = -float('inf'), -float('inf')
        
        for num in nums[m+1:]:
            right = right + num
            max_right = max(max_right, right)
        
        for num in reversed(nums[:m+1]):
            left = left + num
            max_left = max(max_left, left)
            
        return max_left + max_right
    

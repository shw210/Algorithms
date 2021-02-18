写法一：
```Python
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
    
        temp = [0 for _ in range(len(A))]
        self.merge_sort(0, len(A) - 1, A, temp)
        
    def merge_sort(self, start, end, A, temp):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.merge_sort(start, mid , A, temp)
        self.merge_sort(mid + 1, end, A, temp)
        self.merge(start, mid, end, A, temp)
        
    def merge(self, start, mid, end, A, temp):
        left, right = start, mid + 1
        index = start
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right];
                right += 1
                
            index += 1
            
        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1
            
        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1
            
        for index in range(start, end + 1):
            A[index] = temp[index]
```
写法二：
```Python
def mergesort(seq):
        if len(seq) <= 1:
            return seq

        mid = len(seq) // 2  # 将列表分成更小的两个列表
        #左右两个列表进行处理，分别返回两个排序好的列表
        left = mergesort(seq[:mid])
        right = mergesort(seq[mid:])
		# 对排序好的两个列表合并，产生一个新的排序好的列表
        return merge(left, right)
def merge(left, right):
        """合并两个已排序好的列表，产生一个新的已排序好的列表"""
        result = []
        i = 0  # 下标
        j = 0
		# 对两个列表中的元素 两两对比。
		# 将最小的元素，放到result中，并对当前列表下标加1
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else: 
                result.append(right[j])
                j += 1
        
        result += right[j:] 
        result += left[i:]
        return result

```

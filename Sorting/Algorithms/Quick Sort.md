## 写法一
```Python
def partition(self, nums, start, end, pivot_index):
        pivot = nums[pivot_index]
        
        nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
        
        next_small_index = start
        
        for i in range(start, end):
            if nums[i] < pivot:
                nums[i], nums[next_small_index] = nums[next_small_index], nums[i]
                next_small_index += 1
                
        nums[next_small_index], nums[end] = nums[end], nums[next_small_index]
        
        return next_small_index
    
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot_index = random.randint(start, end)
    p = partition(array, start, end, pivot_index)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
```

## 写法二

```Python
def sortIntegers(self, A):
        # write your code here
        if not A: return
    
        return self.quickSort(A, 0, len(A) - 1)
        
    
    def quickSort(self, A, start, end):
        if start >= end: return
        
        pivot = A[start + (end - start) // 2]
        
        left, right = start, end 
        # 注意是 left <= right, 不是 <
        while left <= right:
                                    #注意是 A[left] < pivot, 不是 <=
            while left <= right and A[left] < pivot:
                left += 1 
            
            while left <= right and A[right] > pivot:
                right -= 1 
                
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1 
                right -= 1 
                
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
```

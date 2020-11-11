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

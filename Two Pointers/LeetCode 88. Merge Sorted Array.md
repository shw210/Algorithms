88. Merge Sorted Array
``` Python
while m > 0 and n > 0:
            if nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
            else:
                nums1[m+n-1], nums1[m-1] = nums1[m-1], nums1[m+n-1]
                m -= 1
                
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]
```

思路：从后开始往前loop，如果此刻在未遍历过的值中，nums2的最大值比nums1的最大值大，就把nums2的最大值放到nums1中available的最后的位置，把nums2的指针往前移一位；如果此刻nums2的最大值比比nums1的最大值小，先把nums1的最大值放到available的最后的位置，把nums1的指针往前移一位。 在loop中，avaialbe的最后的位置永远都是 m + n - 1

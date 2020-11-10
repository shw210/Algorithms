#Implementation

L = 0, R = N - 1

ans = -1

while L <= R:
	mid = L + (R - L) // 2
	if a[mid] >= target:
		ans = mid
		R = mid - 1
	else:
		L = mid + 1
		
return ans



''' 
problems suited for binary search: sorted array, looking for some target that satisfied some conditions

General idea: 
0. initialize the answer 
1. go to middle point, if middle point satisfies that condition, record that answer
2. decide which side to go next to find a better answer, if find a better one update the answer
3. loop until go through all the needed scan, ie. L > R


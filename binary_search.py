#python template

# 采取左闭右开的方法


while i < j:     -> [left close, right open)
	mid = (i + j) // 2
	if g(m):    -> here g(m) can be a statement or a function
		i = mid
	else:
		j = mid + 1
return i  

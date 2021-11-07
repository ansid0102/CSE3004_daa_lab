def bs(arr,x):
	low = 0
	high = len(arr)-1

	while low<=high:
		middle = (low+high)//2

		if arr[middle]==x:
			return middle
		elif arr[middle]>x:
			high = middle-1
		else:
			low = middle+1

	return -1


print(bs([1,2,4,7,9,11,15,18],9))

print("Recursive BS")
def bs_rec(A,low,high,key):
	if high < low:
		return low-1
	middle = low + (high-low)//2

	if(key==A[middle]):
		return middle
	elif(key<A[middle]):
		return bs_rec(A,low,middle-1,key)
	else:
		return bs_rec(A,middle+1,high,key)

print(bs_rec([3,5,8,12,15,18,20,20,50,60],1,11,50))
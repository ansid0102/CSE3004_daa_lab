# linear search recursive 
print("Linear Search recursive: \n")
def LinearSearch(A,low,high,key):
	if high<low:
		return "Not Found"
	if A[low]==key:
		print(f"found {key} in index")
		return low
	return LinearSearch(A,low+1,high,key)

print(LinearSearch([10,50,30,70,80,60],1,6,30))
print("\n")

#linear search iterative
print("linear search iterative\n")

def LinearSearchItr(A,low,high,key):
	for i in range(low,high+1):
		if A[i]==key:
			print(f"found {key} in index")
			return i
	return "Not Found"

print(LinearSearchItr([10,50,30,70,80,60],1,6,70))
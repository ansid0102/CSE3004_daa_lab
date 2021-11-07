arr1=[]
arr2=[]
n = int(input())

for i in range(0,n):
	ele = int(input())
	arr1.append(ele)
print("arr2")
k = int(input())

for i in range(0,k):
	ele = int(input())
	arr2.append(ele)

result=[]

def bs(arr1,arr2):
	for i in range(0,k):
		for j in range(0,n):
			if(arr1[j]==arr2[i]):
				return result.append(j)
			else:
				return -1
	return result
print(bs(arr1,arr2))
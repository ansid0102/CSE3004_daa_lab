def max_vote(arr,size):
	for i in range(0,size):
		curr_element = arr[i]
		count = 0
		for j in range(0,size):
			if arr[j]==curr_element:
				count=count+1
		if count > size/2:
			print("Output")
			return 1
	return "Output 0"

size = int(input("Enter size"))
arr=[]
for i in range(0,size):
	ele = int(input())
	arr.append(ele)

print(max_vote(arr,size))
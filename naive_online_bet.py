inp = list()
s, p = [int(i) for i in input().split()]


for i in range(s):
    a, b = [int(i) for i in input().split()]
    inp.append(int(a))
    inp.append(int(b))

points = input().split()
p_list=[]
for i in points:
    p_list.append(int(i))

for i in p_list:
    for j in range(0,len(inp)):
        print("OUTPUT: ")
        if(i>=inp[j] and i<=inp[j+1]):
            print(1)
        else:
            print(0)
        break


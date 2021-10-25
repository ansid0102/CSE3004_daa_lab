def naiveGCD(a,b):
    best = 0
    for d in range(1,a+b+1):
        if(a%d==0 and b%d==0):
            best = d
    return best 
inp = []
for i in range(0,2):
    ele=int(input("Enter: "))
    inp.append(ele)

print(naiveGCD(inp[0],inp[1]))
def EuclidGCD(a,b):
    if b==0:
        return a
    return EuclidGCD(b,a%b)
inp = []
for i in range(0,2):
    ele=int(input("Enter: "))
    inp.append(ele)
print(EuclidGCD(inp[0],inp[1]))
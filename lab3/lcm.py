def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)


def LCM(a,b):
    return (a/GCD(a,b))*b
inp = []
for i in range(0,2):
    ele=int(input("Enter: "))
    inp.append(ele)
print(LCM(inp[0],inp[1]))
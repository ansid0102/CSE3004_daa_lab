def fib_eff(n):
    arr =[0,1]
    for i in range(2,n+1):
        next_num = arr[i-1]+arr[i-2]
        arr.append(next_num)
    return (arr[n]%10)

n=int(input("Enter n: "))
print(fib_eff(n))
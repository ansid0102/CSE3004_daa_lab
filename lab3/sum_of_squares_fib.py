# last digit of sum of squares
def fib_sum_squares(n):
    arr =[0,1]
    sum=1
    for i in range(2,n+1):
        next_num = arr[i-1]+arr[i-2]
        sum=sum+(next_num*next_num)
        arr.append(next_num)
    return (sum%10)
n= int(input("Enter n: "))
print(fib_sum_squares(n))
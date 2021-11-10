    

def moneyChange(x):
    denominations=[1,5,10]
    denominations.sort(reverse=True)
    i=0
    count=0
    while(x>0):
        if(denominations[i]>x):
            i=i+1
        else:
            count+=1
            print(str(denominations[i]))
            x -= denominations[i]
    print(f"The min coins are {count}")


moneyChange(28)

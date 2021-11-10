# reaching back round trip 
def car_fueling_reachback(dist,miles,n,gas_stations):
    min_refill,last_refill, curr_refill,flag= 0,0,0,0,
    reach_back = dist-gas_stations[n-1]
    while curr_refill <=n:  
        last_refill=curr_refill
        while(curr_refill<=n and (gas_stations[curr_refill+1]-gas_stations[last_refill])<=miles):
            curr_refill+=1
            if(curr_refill==last_refill):
                print("Not possible")
                flag=1
                break
            if(curr_refill<=n):
                min_refill+=1
        if(flag==0):
            saved = miles-(gas_stations[curr_refill]-gas_stations[last_refill])
        print(min_refill)
        print(saved)
        if(saved>=(dist-gas_stations[n])):
            print("Successful")
        else:
            print("Not Successful")        

print(car_fueling_reachback(600,250,3,[200,350,440]))

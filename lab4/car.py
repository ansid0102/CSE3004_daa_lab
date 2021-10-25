# car Fuelling

# d miles 
def car_fuelling(dist.miles,n,fuel_s):
    refil_count,cur_refill,limit = 0
    while(limit < dist):
        if cur_refill >= n or fuel_s[cur_refill]>limit:
            return -1
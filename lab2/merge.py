def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2 

        L = arr[:mid]#left half
        R = arr[mid:]#right half

        mergeSort(L)
        mergeSort(R)

        i = j = k =0

        while(i<len(L) and j<len(R)):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  

def listPrint(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__ == '__main__':
    arr=[19,13,5,14,9,11,1]
    print("Given Array")
    listPrint(arr)
    mergeSort(arr)
    print(f"Sorted Array is {arr}")

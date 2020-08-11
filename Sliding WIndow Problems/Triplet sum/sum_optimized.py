import time

def triple_sum(arr,x):
    arr.sort()
    for i in range(len(arr)):
        temp = x - arr[i]
        for j in range(i+1,len(arr)):
            l,r = i+1,len(arr)-1
            while l<r:
                if arr[l]+arr[r]==temp:
                    print(arr[i],arr[l],arr[r])
                    return True
                elif arr[l]+arr[r]<temp:
                    l+=1
                elif arr[l]+arr[r]>temp:
                    r-=1
    else:
        return False
                    
if __name__ == "__main__":
    start = time.time()
    test_arr = [1, 4, 45, 6, 10, 8] 
    sum = 22
    triple_sum(test_arr,sum)
    print("Time taken is ",time.time()-start)
    
            

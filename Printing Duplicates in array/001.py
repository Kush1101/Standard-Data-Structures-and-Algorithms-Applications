# From range 0 to n-1
# Here we will use the Hash set to find all the duplicates in an array.
# This will take O(n) time.

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
    
        if arr[abs(arr[i])]>0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            duplicates.append(arr[abs(arr[i])])
    return duplicates        
        
            

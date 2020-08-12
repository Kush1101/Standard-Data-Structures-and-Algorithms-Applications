# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:39:26 2020

@author: DeLL
"""
import random_objects
def find_triplet(arr):
    arr.sort()
    for i in range(len(arr)-1,-1,-1):
        temp = arr[i]
        l,r = 0,i-1
        while l<r:
            if arr[l]+arr[r]==temp:
                return (arr[l],arr[r],temp)
            if arr[l]+arr[r]<temp:
                l+=1
            if arr[l]+arr[r]>temp:
                r-=1
    return -1

if __name__=='__main__':
    test_arr = random_objects.random_list(10,1,100)
    print(test_arr)
    print(find_triplet(test_arr))
    
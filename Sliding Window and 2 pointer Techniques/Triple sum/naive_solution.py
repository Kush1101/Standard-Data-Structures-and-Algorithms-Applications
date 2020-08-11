# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:46:17 2020

@author: DeLL
"""
import time
import random_objects
def naive_solution(arr,x):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k]==x:
                    return (arr[i],arr[j],arr[k])
    else:
        return -1

if __name__=="__main__":
    start = time.time()
    test_arr = random_objects.random_list(10,1,100)
    print(test_arr)
    summ = random_objects.random_integer(1,50)
    print(summ)
    print(naive_solution(test_arr,summ))  
    print("Completed in ",time.time()-start)
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:33:05 2024

@author: admin
"""

def generate_sorted_list(start,end,step):
    return list(range(start,end+1,step))

numbers=generate_sorted_list(0,100,2)
print('sorted_list:',numbers)

def binary_search(arr,target):
    left,right=0, len(arr)-1
    while left <= right:
        mid =(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid-1
            
    return -1

def main():
    numbers=generate_sorted_list(0,100,2)
    print('soryed_list:',numbers)
    
    target=int(input('Enter the number to search for: '))
    index=binary_search(numbers, target)
    
    if index != -1:
        print(f'Number {target} found at index {index}.')
    else:
        print(f'Number{target} not found in the list.')
        
    if __name__=='__main__':
        main()
            
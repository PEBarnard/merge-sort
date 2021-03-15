# Author: Pieter Barnard
# Date: 15-03-2021
# Project description: Merge Sort algorithm solved using recursion. Running time is O(n log n)
# e-mail: pieterebarnard@gmail.com

import random
import time

class MergeSort:
    def sort(self, arr):
        if len(arr) == 1:
            return arr
        
        mid = self.get_middle(arr)
        right = arr[mid:len(arr)]
        left = arr[0: mid]
        right_list = self.sort(right)
        left_list = self.sort(left)
        return self.merge(left_list, right_list)
  
    def get_middle(self, arr):
        return len(arr)//2
   
    def merge(self, left_list, right_list):
        if len(left_list) == 0:
            return right_list
        if len(right_list) == 0:
            return left_list
        
        if left_list[0] <= right_list[0]:
            
            left_list[1:] = self.merge(left_list[1:], right_list)
            return left_list
        else:
            right_list[1:] = self.merge(left_list, right_list[1:])
            return right_list
            
def main():
    start = time.time_ns()
    arr = [random.randint(1, 300000) for a in range(500)]
    ms = MergeSort()
    print(ms.sort(arr))
    print(f"Running time = {(time.time_ns() - start)/1000000000} seconds")

if __name__ == '__main__':
    main()
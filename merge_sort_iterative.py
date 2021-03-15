# Author: Pieter Barnard
# Date: 15-03-2021
# Project description: Merge Sort algorithm solved using iteration. Running time is O(n log n)
# e-mail: pieterebarnard@gmail.com

import random
import time

class MergeSort:   
    def sort(self, nums):
        stack = [nums]
        arr_merge = []
        
        while stack:
            arr = stack.pop()
            mid = self.get_middle(arr)  
            if len(arr) == 1:
                arr_merge.append(arr)
            else:
                stack.append(arr[mid:len(arr)])
                stack.append(arr[0: mid])

        del stack
        return self.merge(arr_merge)
    
    def get_middle(self, arr):
        return len(arr)//2
    
    def _should_continue(self, q, s):
        if not len(q) != s:
            return False
        return True
    
    def merge(self, m_queue):

        l = len(m_queue)
        temp = []
        while m_queue:
            left_ = m_queue.pop(0)
            if len(left_) == l:
                m_queue = left_
                break
            right_ = m_queue.pop(0)

            while len(left_) != 0 and len(right_) != 0:
                if left_[0] <= right_[0]:
                    temp.append(left_.pop(0))
                    if len(left_) == 0:
                        temp.extend(right_)
                else:
                    temp.append(right_.pop(0))
                    if len(right_) == 0:
                        temp.extend(left_)

            m_queue.append(temp.copy())
            temp.clear()
        
        del temp
        return m_queue

def main():

    start = time.time_ns()
    arr = [random.randint(1, 1000000) for a in range(5000)]
    ms = MergeSort()
    # print(ms.sort(arr))
    print(f"Running time = {(time.time_ns() - start)/1000000000} seconds")

if __name__ == '__main__':
    main()

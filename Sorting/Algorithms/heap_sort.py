# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:49:57 2020

"""

def heapify(A, n, i):
    # each heapify function is a top-to-bottom process
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if (left < n and A[left] > A[largest]):
        largest = left
    if (right < n and A[right] > A[largest]):
        largest = right
        
    if largest != i:
        A[largest], A[i] = A[i], A[largest]        
        heapify(A, n, largest)
        
def heap_sort(A):
    n = len(A)
    # build max_heap using heapify function from bottom to top, i.e. in the loop, we build heap at the bottom first, and then go up to build heap at a higher level
    for i in range(n//2 - 1, -1, -1):
        heapify(A, n, i)
        
    # sort by keep removing the first element of the max_heap
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
    
A = [ 3, 1, 7, 3, -4, 28, 9]        
heap_sort(A)

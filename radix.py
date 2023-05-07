# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:53:11 2023

@author: Hannah
"""

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
#def radixSort(array):
 #   # Get maximum element
 #   max_element = max(array)

    # Apply counting sort to sort elements based on place value.
  #  place = 1
   # while max_element // place > 0:
    #    countingSort(array, place)
     #   place *= 10
        

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    # Do radix sort using counting sort as the sorting algorithm
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    # Create a count array to store count of individual digits
    count = [0] * 10
    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    # Change count[i] so that it now contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i-1]
    # Build the output array
    output = [0] * n
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    # Copy the output array to arr[]
    for i in range(n):
        arr[i] = output[i]
    return arr


        
array = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", array)
sorted_array = radix_sort(array)
print("Sorted array:", sorted_array)




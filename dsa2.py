# 1.Implement Binary Search -------------------------------------------------------

def binary_search(array,a,low,high):
   
    while low <= high:
        mid = low + (high-low)//2
        
        if array[mid] == a:
            return mid
        
        elif array[mid] > a:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1

array=[1,2,3,4,5,6,7,8,9,10]
print("The given array is: ",array)
a = 5
index = binary_search(array,a,0,len(array)-1)
if index != -1:
    print("The index of the element is " + str(index))
else:
    print("Element Not found")  


#  2.Implement merge sort--------------------------------------------------------------------------------------

def mergesort(array):
    if len(array) > 1:
        mid = len(array)//2
        sub_array1 = array[:mid]
        sub_array2 = array[mid:]

        mergesort(sub_array1)
        mergesort(sub_array2)

        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                array[k] = sub_array1[i]
                i += 1
            else:
                array[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len (sub_array1):
            array[k] = sub_array1[i]
            i += 1
            k += 1
        while j < len(sub_array2):
            array[k] = sub_array2[j]
            j += 1
            k += 1

array = [7,8,9,12,4,3,2,1]
mergesort(array)
print(array) 


#3.Implement Quick Sort---------------------------------------------------------------------------------------

def Quicksort(array):
            elements = len(array)
            if elements < 2:
                      return array
            current_position = 0
            for i in range(1,elements):
                    if array[i] <= array[0]:  
                      current_position += 1
                      temp = array[i]
                      array[i] = array[current_position]
                      array[current_position] = temp
            temp = array[0]
            array[0] = array[current_position]
            array[current_position] = temp
            left = Quicksort(array[0:current_position])
            right = Quicksort(array[current_position+1:elements])
            array = left + [array[current_position]] + right
            return array
array_to_be_sorted = [4,27,3,1,6]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",Quicksort(array_to_be_sorted)) 


# #4.Implement Insertion Sort-------------------------------------------------------------------------

def insertionsort(array):
    if (n := len(array)) <= 1:
        return
    for i in range(1,n):
        key = array[i]
        j = i - 1
        while j >= 0 and key <array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

array = [6,8,9,3,5,2,10]
insertionsort(array)
print(array) 

# #5.Write a program to sort list of strings (similar to that of dictionary)-----------------------------------------------------
 
  
list_a= [{'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr'}]

# Using sort() function
list_a.sort()
 
print(list_a)
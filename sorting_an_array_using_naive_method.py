########################################################################################################################
#                                   Challenge 2 - Sorting an array (using Bubble sort technique)
########################################################################################################################

# Input the size of an array
size_of_array = int(input("Enter the size of an array : "))

# Getting the elements of the array from the user
print("Enter the space separated elements for the array :")
# Assigning the elements to the list named array
array = list(map(int,input().split(' ')))[:size_of_array]

# Print the array befor sorting
print(f"Array before sorting : {array}")

# Using Bubble sort technique to sort the array
for i in range(size_of_array):
    for j in range(0,size_of_array - i - 1):
        #Checking whether the current element is greater than the next element then swap
        if array[j] > array[j+1] :
            # Swapping the corresponding elements with the help of temporary variable
            temp = array[j+1]
            array[j+1] = array[j]
            array[j] = temp

# Print the array after sorting
print(f"Sorted Array : {array}")

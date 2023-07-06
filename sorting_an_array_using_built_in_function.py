########################################################################################################################
#                                   Challenge 2 - Sorting an array (using Build-in function)
########################################################################################################################

# Input the size of an array
size_of_array = int(input("Enter the size of an array : "))

# Getting the elements of the array from the user
print("Enter the space separated elements for the array :")
# Assigning the elements to the list named array
array = list(map(int,input().split(' ')))[:size_of_array]

# Print the array befor sorting
print(f"Array before sorting : {array}")
array.sort()

# Print the array after sorting
print(f"Sorted Array : {array}")

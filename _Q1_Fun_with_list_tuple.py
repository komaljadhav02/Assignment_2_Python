#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

size = int(input("Enter the size of the list: "))  #Taking input from user
lst = []
org_list = []

for i in range(size):
    values = input("Enter the values: ")  #Taking tuple values from user
    tuple_values = tuple(map(int, values.split(',')))
    lst.append(tuple_values) 

sorted_list = []

while lst:
    min_tuple = lst[0]
    for j in lst:
        if j[-1] < min_tuple[-1]:
            min_tuple = j
    sorted_list.append(min_tuple)
    lst.remove(min_tuple)
print("Sorted list:", sorted_list)
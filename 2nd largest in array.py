list1 = [10,20,20,4,45,45,99]

list2 = list(set(list1))
list2.sort()
print("second largest element is :",list2[-2])

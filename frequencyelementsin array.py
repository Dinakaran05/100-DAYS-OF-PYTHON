from collections import Counter

def print_frequency(arr):
    
    frequency_counter = Counter(arr)
    
    
    for element, count in frequency_counter.items():
        print("Element", element, "occurs", count, "times")

my_array = [1,2,2,3,3,3,4,4,4,4]
print_frequency(my_array)

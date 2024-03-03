Input_number = 6
Sum = 0
for i in range(1, Input_number):
    if(Input_number % i == 0):
        Sum = Sum + i
if (Sum == Input_number):
    print("Number is a Perfect Number")
else:
    print("Number is not a perfect number")

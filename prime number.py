start_limit = int(input("Enter start limit:"))
end_limit = int(input("Enter end limit:"))

for no in range(start_limit,end_limit+1):
    if no>1:
        count = 0
        for i in range(2,no):
            if no % i == 0:
                count = count + 1
        if count == 0:
            print(no)

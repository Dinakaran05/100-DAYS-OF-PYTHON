num = 1221
temp = num
reverse = 0
while > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
    print("palindrome")
else:
    print("not a palindrome")

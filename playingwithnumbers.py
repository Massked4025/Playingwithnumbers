number = int(input("Enter the number: "))
temp = number
reverse_number = 0

while temp>0:
    digit = temp%10
    reverse_number = reverse_number * 10 + digit
    temp //= 10

if number== reverse_number:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")

#HCF

largestnumber = int(input("Enter the largest number: "))
smallestnumber = int(input("Enter the smallest number: "))

while smallestnumber:
    numberstore = smallestnumber
    smallestnumber = largestnumber%smallestnumber
    largestnumber = numberstore

print("HCF is", largestnumber)
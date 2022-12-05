
count = 0
largest_num = float("-inf")
smallest_num = float("+inf")
second_largest = float("+inf")

while count < 5:
    num = int(input("Enter your number: "))
    if num > largest_num:
         largest_num = num
    if num < smallest_num:
        smallest_num = num
    if largest_num > num > second_largest:
        smallest_num = second_largest
        num == second_largest
    count += 1

print("largest number is: " , largest_num)
print("smallest number is : " , smallest_num)
print("second largest number is: ",second_largest)

largest_so_far = 0
second_largest_so_far = 0
smallest_num = 0
count = 0


while count < 5:
      num = int(input("Give me a number: "))

      if num > largest_so_far:
        second_largest_so_far = largest_so_far
        largest_so_far = num
      if num > second_largest_so_far and num < largest_so_far:
        second_largest_so_far = num
      if num <  second_largest_so_far and num < smallest_num:
         smallest_num = num
      count += 1

print("The largest number is", largest_so_far)
print("The second largest number is", second_largest_so_far)
print("The smallest number is",smallest_num)
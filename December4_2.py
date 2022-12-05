total = 0
positive_count = 0
negative_count = 0
counter = 0
average = 0
sum_of_positive_count = 0
sum_of_negative_count = 0
number = int(input("Enter a number,0 to exit: "))
while number != 0:
    if number > 0:
        positive_count = positive_count + 1
        sum_of_positive_count += number
    if number < 0:
        negative_count += 1
        sum_of_negative_count += number
    number = int(input("Enter a number,0 to exit: "))
    counter= counter + 1

total = sum_of_positive_count + sum_of_negative_count
average = total /counter
print(f"The number of positive is {positive_count}\nThe number of negative is {negative_count}"
      f"\nThe sum of positive numbers is {sum_of_positive_count}\nThe sum of negative numbers is {sum_of_negative_count}"
      f"\nThe total is {total}\nThe average is {average}")


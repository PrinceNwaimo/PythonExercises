# 6 (Odd or Even) Use if statements to determine whether an integer is
# odd or even. [Hint: Use the remainder operator. An even number is a
# multiple of 2. Any multiple of 2 leaves a remainder of 0 when divided by
# 2.]#
number = int(input("pick a number: "))
even_number = number % 2
if (number % 2 == 0):
    print("This is an even number")
else:
    print("This is an odd number")
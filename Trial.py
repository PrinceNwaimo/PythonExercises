number = 0
count = 0

while number < 100:
    number = number+1
    count +1
    if (number % 15 == 0):
        print("FizzBuzz")
    elif(number % 3==0):
        print("Fizz")
    elif(number % 5==0):
        print("Buzz")

    else:
        print(number)

# simple while

x: int = 0    # initialize loop-control variable

#  test loop-control variable at beginning of loop
while x <= 10:
    print(x, end="  ")   #print the value of x each time through the while loop
    x += 1

print()
print("The final value of x is", x)
#score=int(input("Enter a score or -1 to exit: "))

#while score != -1:
    #print(score)
    #score= int(input("Enter a score or -1 to exit: "))
    # In java if you do not want to repeat the last statement, you use a do - while loop.
    #using a walrus operator(assignment expression)

while (score := int(input("Enter  a score or -1 to exit: "))) != -1:
 print(score)


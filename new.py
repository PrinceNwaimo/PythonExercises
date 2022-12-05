#tiples) Use if statements to determine whether 1024 is a multiple
#of 4 and whether 2 is a multiple of 10. (Hint: Use the remainder operator.)#

multiple  = int(input("multiple: "))
factor = int(input("factor: "))

if (multiple % factor == 0):
    print("It is a multiple")
else:
    print("It is not a multiple")

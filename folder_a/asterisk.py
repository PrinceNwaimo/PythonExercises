def print_star(x):
    blank = 0
    for i in range(1, x+1, 2):
        for j in range(blank,x):
            print(" ",end="")
        for k in range(0, i):
            print("x",end="")
        blank = blank + 1
        print()


def print_star2(x):
    blank = x-(x-3)
    for i in range(x-2, 0, -2):
        for j in range(x, blank, -1):
            print(" ",end="")
        for k in range (i, 0, -1):
            print(f'{"x"}', end="")
        blank = blank - 1
        print()


print_star(7)
print_star2(7)
s = "hello world"

#for i in range(len(s)):
    #print(f"{s[i]}")
    #print(f"{s[i]}was found at index{i}")

to_be_found = "l"
#for i in range(len(s)):
#    if s[i] == to_be_found:
#        print(f"{s[i]} was found at index {i}")
#else:
#    print(F"sorry I could not find your entry'{to_be_found}'")

for index, letter in enumerate(s):

    if letter == to_be_found:
        print(f"{letter} found at index{index}")
        break
else:
    print(-1)

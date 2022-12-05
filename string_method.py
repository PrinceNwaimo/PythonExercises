hello = "Hello there!!!"
# print(hello.rfind("e"))
#  print(hello.upper())
#  print(hello.lower())
#  print(hello.title())
#  print(hello.capitalize())
#  print(hello.casefold())
#  print(hello.swapcase())
# print(hello.count("e"))

# #strings like hello are unchangeable e.g
# print(hello.lower().count("e"))
# print(hello.center(50))
# print(hello.center(50,"*"))
# print(hello.ljust(20,"x"))
# print(hello.rjust(20,"*"))
#print(hello.find("llo"))
#print(hello.index("l"))
# check note for difference between the find and index#
#print(hello.find("e",3,5))
# found = 0
# while True:
#     found = hello.find("e",found)
#     if found == -1:
#         break
#     print(found)
#
#     found+= 1
#print(hello.endswith("!!!"))
print(hello.replace("l","r"))
print(hello.replace("l","r",1,))
bin_ ="101100011001011110"
print(bin_.replace("1","X").replace("0","1").replace("X","0"))
print(bin_.translate(str.maketrans("01","07","8")))
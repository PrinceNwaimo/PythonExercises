# array=[]
# for i in range(5):
#     array.append("Hi")#use append to add
#     print(array)
#     array.insert(3,"Hello")
#     array.clear()
#     print(array)
#     c14=array.copy()
#     print(c14)
#     array.count("Hi")
#      print(c14)

#   set
set_values = {"Hi", "Hello", "Glo", "Get"}
user_input = list(input("Enter a number: "))
print(user_input)
count = 0
for i in range(len(user_input)):
    if user_input[i] != set_values:
        set_values.add(user_input[i])
    else:
        count = len(set_values)
        print(user_input[i])
print("set --> ", set_values,count)

name = "king"
age = 18

s = "{} is {} years old".format(name,age)
s = "{0:^20} is {1} years old,and {0} loves {2}".format(name,age,"java")
s = f"{name=} is {age:>.2f} years old,and {name} loves {'Java'}"
print(s)
hello = "hello world"
for index, letter in enumerate(hello,start=1):
    print(f"{letter}--->{index}")


for i in range(1,21,1):
    s="*" * i
    print(f"{s:25}{s:^25}{s:>25}")



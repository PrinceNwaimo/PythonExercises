minutes = int(input("Enter number in minutes: "))
years = minutes // 525600,
days = minutes % 525600 // 1440,
print(minutes,"minutes is approximately", " " , years,"years" , " " , "and",  " ",days,"days")
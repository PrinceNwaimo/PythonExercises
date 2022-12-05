word = "Hello boss baby"
to_be_found= "b"
for i in range(len(word)):
 print(i)

 if word[i] == to_be_found:

  print(f"{word[i]} was found at index {i}")
to_be_found ="b"
print(f"{word}")
print(f"{word}".replace("b"," "))


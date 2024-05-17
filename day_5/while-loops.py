

i = 0
while i < 5:
    print(i)
    i += 1



count = 0
while True:
    print(count)
    count += 1
    if count == 3:
        break


num = 0
while num < 6:
    num += 1
    if num % 2 == 0:
        continue
    print(num)


x = 10
while x > 0:
    print(x)
    x -= 1
    
    
    password = ""
while password != "secret":
    password = input("Enter the password: ")
print("Access granted")


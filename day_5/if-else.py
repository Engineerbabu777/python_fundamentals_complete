

age = 18
if age >= 18:
    print("You are an adult")


number = 5
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


score = 85
if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("Fail")


num = 10
if num > 0:
    print("Positive number")
    if num > 5:
        print("Greater than 5")
    else:
        print("Less than or equal to 5")
else:
    print("Non-positive number")


is_logged_in = True
message = "Welcome back!" if is_logged_in else "Please log in"
print(message)

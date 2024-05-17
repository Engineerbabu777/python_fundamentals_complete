

add = lambda x, y: x + y
print(add(3, 5))


numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)


numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

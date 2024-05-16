# Example demonstrating sets in Python

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 3, 4, 5}
print("Set with duplicates removed:", duplicate_set)

# Adding elements to a set
my_set.add(6)
print("Set after adding element:", my_set)

# Removing elements from a set
my_set.remove(3)
print("Set after removing element:", my_set)

# Checking if an element is in a set
print("Is 4 in the set?", 4 in my_set)

# Set operations: union, intersection, difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference of sets (set1 - set2):", difference_set)

# Checking if a set is a subset or superset of another set
subset_check = {1, 2}.issubset(set1)
print("{1, 2} is a subset of set1:", subset_check)

superset_check = set1.issuperset({1, 2})
print("set1 is a superset of {1, 2}:", superset_check)

# Set comprehension
even_numbers = {x for x in range(10) if x % 2 == 0}
print("Set of even numbers less than 10:", even_numbers)

# Set methods
example_set = {1, 2, 3, 4, 5, 3, 3}

# Adding multiple elements
example_set.update({6, 7, 8})
print("Set after adding multiple elements:", example_set)

# Removing element using discard (doesn't raise an error if element not present)
example_set.discard(3)
print("Set after discarding element:", example_set)

# Removing all elements
example_set.clear()
print("Set after clearing all elements:", example_set)

# Example demonstrating dictionaries in Python

# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values using keys
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Adding new key-value pairs
my_dict['gender'] = 'Male'
print("Dictionary after adding a new key-value pair:", my_dict)

# Modifying values
my_dict['age'] = 35
print("Dictionary after modifying a value:", my_dict)

# Removing key-value pairs
removed_value = my_dict.pop('city')
print("Dictionary after removing a key-value pair:", my_dict)
print("Removed value:", removed_value)

# Checking if a key is present in the dictionary
print("Is 'age' a key in the dictionary?", 'age' in my_dict)

# Dictionary methods
# Keys method - returns a view object containing the keys of the dictionary
keys_view = my_dict.keys()
print("Keys view:", keys_view)

# Values method - returns a view object containing the values of the dictionary
values_view = my_dict.values()
print("Values view:", values_view)

# Items method - returns a view object containing the key-value pairs of the dictionary as tuples
items_view = my_dict.items()
print("Items view:", items_view)

# Copy method - returns a shallow copy of the dictionary
copied_dict = my_dict.copy()
print("Shallow copy of the dictionary:", copied_dict)

# Clear method - removes all key-value pairs from the dictionary
my_dict.clear()
print("Dictionary after clearing all key-value pairs:", my_dict)

# Dictionary comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]

comprehension_dict = {k: v for k, v in zip(keys, values)}
print("Dictionary created using comprehension:", comprehension_dict)

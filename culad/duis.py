def my_generator():
    yield [7, 19, 0.002833835380796783]

# Create an instance of the generator
gen = my_generator()

# Use the next() function to retrieve the next value from the generator
value = next(gen)
print(value)  # Output: [7, 19, 0.002833835380796783]

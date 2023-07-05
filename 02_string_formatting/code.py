name = "Bob"
greeting = "Hello, Bob"

print(greeting) #Hello, Bob

name = "Rolf"

print(greeting) #Hello, Bob

greeting = f"Hello, {name}"
print(greeting) #Hello, Rolf

# --

name = "Anne"
print( greeting)  # Hello, Rolf
print(f"Hello, {name}")  # Hello, Anne

# -- Using .format() --

# We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.

greeting = "Hello, {}"
with_name = greeting.format("Rolf")
print(with_name) #Hello, Rolf

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted) #Hello, Rolf. Today is Monday.
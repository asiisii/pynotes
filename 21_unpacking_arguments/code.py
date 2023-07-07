def multiply(*args):  #*args -> creates a tuple (3,5) and (-1,)
    print(args) #(3,5) & (-1,)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(3, 5)) #15
print(multiply(-1)) # -1 

# The asterisk takes all the arguments and packs them into a tuple.
# The asterisk can be used to unpack sequences into arguments too!

def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))  # instead of add(nums[0], nums[1])

# -- Uses with keyword arguments --
# Double asterisk packs or unpacks keyword arguments

def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}

print(add(**nums))

# -- Forced named parameter --

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total

# *args = basically  collects all the arugments but operator
def apply(*args, operator): #we will need to pass an argument thats called "operator"
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 5, "+"))  # Error because we didn't pass an arugment called operator
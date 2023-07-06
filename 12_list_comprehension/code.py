numbers = [1, 3, 5]
new_arr = []
#  do this 
squares = [x * 2 for x in numbers]
# instead of 
for num in numbers:
    new_arr.append(num * 2)

# -- Dealing with strings --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Can make a new list of friends whose name starts with S --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# -- List comprehension creates a _new_ list --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s) #returns False because they're not same lists and are in two different places in our computer memory even though elements are same
print("friends: ", id(friends), " starts_s: ", id(starts_s)) #friends:  4534743424  starts_s:  4534738944
# id is the memory address
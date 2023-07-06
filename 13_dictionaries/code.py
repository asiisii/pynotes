friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Bob"] = 20

print(friend_ages)  # {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}
print(friend_ages["Bob"])

# -- List of dictionaries --

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(friends)

# -- Iteration --

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}%")

# Better
print("item method", student_attendance.items()) # item method dict_items([('Rolf', 96), ('Bob', 80), ('Anne', 100)])
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# -- Using the `in` keyword --

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob isn't a student in this class!")

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values)) #92.0
print(attendace_values) #dict_values([96, 80, 100])
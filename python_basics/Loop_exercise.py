

"""""
i = "hi"


#for range is set to go from 5 to 10 with a step size of 2
for i in range(5, 10, 2):
    print("hi", i)


#101 + 5*2 = 111    [101, 103, 105, 107, 109, 111, 113, 115, 117, 119]

l = []
for i in range(10):
    l.append(101 + (i * 2))
print(l)
"""""

"""""
l = []
incr = 0
current_val = 0
while incr < 15:
    print("current value at beginning loop:",current_val)
    current_val = current_val + incr
    
    l.append(current_val)
    incr = incr + 1
    print("increment at end of loop:", incr)

print(l)

"""""

l = []

for i in range(10):
    l.append(10 + i * 3)

print(l)

l = []

for i in range(10):
    l.append(i * 2)

print(l)

# Initialize an empty list
l = []

# Define the range of values to repeat
for i in range(0, 11, 2):
    l.append(i)

# Repeat the pattern a certain number of times (e.g., 3 times)
repeated_pattern = l * 3

print(repeated_pattern)


# Initialize an empty list
l = []

# Outer loop to repeat the pattern a certain number of times
for _ in range(3):  # Adjust the range to change the number of repetitions
    # Inner loop to generate the sequence 0, 2, 4, 6, 8, 10
    for i in range(0, 11, 2):
        l.append(i)

print(l)

l = []
while i < 10:
    l.append



# Initialize an empty list
pattern = []

# Define the number of repetitions for the complete pattern
num_repeats = 2  # Adjust this for more or fewer repeats
current_repeat = 0

# Use a while loop to control the number of repetitions
while current_repeat < num_repeats:
    # First ascending part
    i = 0
    while i <= 10:
        pattern.append(i)
        i += 2  # Increment by 2
    
    # Descending part
    i = 8
    while i >= 0:
        pattern.append(i)
        i -= 2  # Decrement by 2
    
    current_repeat += 1  # Move to the next repeat

print(pattern)


num_iterations = []

for i in num_iterations:
    num_splits = 2 ^ i
    for j in range(num_splits):
        index = j * 2
        print(index)




bpm = 100

# Initialize lists
events1 = []
events2 = []

# Function to prepare events, with dynamic input prompt
def prepareEvents(events, list_name):
    amountofevents = int(input(f"How many events for {list_name}?  "))
    
    for i in range(int(amountofevents)):
        events.append(float(input(f"Enter event duration in sixteenths \nFor {list_name}, sixteenth {i+1}:")))
    
# Call the function for each list with a dynamic name
prepareEvents(events1, "List 1")
prepareEvents(events2, "List 2")

"""
while True:

     if user_input == 'no':
        print(f"Using default BPM: {bpm}")
        break  # Exit the loop and use the current bpm (default)
    
    try:
        bpm = int(input(f"current bpm: {bpm},\nnew bpm?: "))
        break  # If input is valid, break out of the loop
    except ValueError:
        print("Invalid input. Please enter a valid integer for BPM.")
"""
while True:
    user_input = input(f"Current BPM: {bpm},\nNew BPM? (or type 'no' to use default): ").strip().lower()
    
    if user_input == 'no':
        print(f"Using default BPM: {bpm}")
        break  # Exit the loop and use the current bpm (default)
    
    try:
        bpm = int(user_input)  # Try to convert input to an integer
        break  # If input is valid, break out of the loop
    except ValueError:
        print("Invalid input. Please enter a valid integer for BPM or 'no' to use the default.")





#translate 16th value to time value
sixteenthnotedur = 60 / (bpm*4)
print("sixteenthnotedur:", sixteenthnotedur)



#Turn event duration into corresponding value of sixteenth
def multiply_by_16th(events, sixteenthnotedur):
    for i in range(len(events)):
        events[i] = events[i] * sixteenthnotedur 
    #return [event * sixteenthnotedur for event in events]


multiply_by_16th(events1, sixteenthnotedur)
multiply_by_16th(events2, sixteenthnotedur)
print("new list of events1, sixteenths in ms", events1)
print("new list of events2, sixteenths in ms", events2)

#[{'kick':soundFile, 'ts':200},{snare, 300}, kick]

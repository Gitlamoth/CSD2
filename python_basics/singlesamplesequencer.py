

bpm = 100


amountofevents = int(input("how many events? "))
events = []

for i in range(int(amountofevents)):
    events.append(float(input(f"Enter event duration in sixteenths \nsixteenth {i+1}:")))
    


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

events_to_sixteenth = []

#Turn event duration into corresponding value of sixteenth
def multiply_by_16th(events, sixteenthnotedur):
    
    return [event * sixteenthnotedur for event in events]

events = multiply_by_16th(events, sixteenthnotedur)
print("new list of events, sixteenths in ms", events)


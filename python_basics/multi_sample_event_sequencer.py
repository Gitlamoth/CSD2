import simpleaudio as sa
import time

# load sample
soundFile = sa.WaveObject.from_wave_file("./hat.wav")

bpm = 100

# Input for BPM
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

# Initialize lists
events1 = []
events2 = []

# Function to prepare events, with dynamic input prompt
def prepareEvents(events, list_name):
    while True:
        try:
            amountofevents = int(input(f"How many events for {list_name}?  "))
            break  # Exit loop when valid input is received
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(amountofevents):
        while True:
            try:
                event_duration = float(input(f"Enter event duration in sixteenths \nFor {list_name}, event {i + 1}: "))
                events.append(event_duration)
                break  # Break on valid input
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Define initial instrument notes
initial_instrument_1_notes = [
    {'instrument': 'Instrument_1', 'sample_location': './hat.wav'},
  
]

initial_instrument_2_notes = [
    {'instrument': 'Instrument_2', 'sample_location': './hat.wav'},
 
]

# Prepare events for both instruments
prepareEvents(events1, "List 1")
prepareEvents(events2, "List 2")

# Stretch notes to match the number of events
def stretch_notes(instrument_notes, target_count):
    while len(instrument_notes) < target_count:
        # Duplicate the last note if not enough
        instrument_notes.append(instrument_notes[-1].copy())

# Stretch both instrument notes based on event counts
stretch_notes(initial_instrument_1_notes, len(events1))
stretch_notes(initial_instrument_2_notes, len(events2))

# Translate 16th value to time value
sixteenthnotedur = 60 / (bpm * 4)
print("sixteenthnotedur:", sixteenthnotedur)

# Turn event duration into corresponding value of sixteenth
def multiply_by_16th(events, sixteenthnotedur):
    return [event * sixteenthnotedur for event in events]

# Generate timestamps and durations for events
events1 = multiply_by_16th(events1, sixteenthnotedur)
events2 = multiply_by_16th(events2, sixteenthnotedur)

# Assign timestamps to each instrument's notes
for note, timestamp in zip(initial_instrument_1_notes, events1):
    note['timestamp'] = timestamp
    note['duration'] = timestamp  # For now, we're setting the duration same as timestamp (you can change this logic)

for note, timestamp in zip(initial_instrument_2_notes, events2):
    note['timestamp'] = timestamp
    note['duration'] = timestamp

# Combine the notes into one list for playback
combined_notes = initial_instrument_1_notes + initial_instrument_2_notes

# Function to sort notes by timestamp
def sort_notes_by_timestamp(notes):
    notes.sort(key=lambda x: x.get('timestamp', 0))

# Call the sorting function
sort_notes_by_timestamp(combined_notes)

# Read and print out all timestamps from the dictionaries in combined_notes
for note in combined_notes:
    print(f"Instrument: {note['instrument']}, Sample: {note['sample_location']}, Timestamp: {note['timestamp']} seconds, Duration: {note['duration']} seconds")


# Store the start time
time_zero = time.time()

# iterate through time sequence and play sample
while combined_notes:
    now = time.time() - time_zero
    ts = combined_notes[0]['timestamp']  # Check the timestamp of the next event
    duration = combined_notes[0]['duration']  # Get the duration of the note

    # check if we passed the next timestamp,
    # if so, play sample and fetch new timestamp
    if now >= ts:
        play_obj = soundFile.play()  # Play the sound asynchronously
        time.sleep(duration)  # Sleep for the duration of the note to simulate length
        play_obj.wait_done()  # Wait for the sound to finish before proceeding
        combined_notes.pop(0)  # Only pop after playing the sound and its duration

    time.sleep(0.001)  # Sleep to avoid busy waiting

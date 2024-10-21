import simpleaudio as sa
import time
import random

# load sample
soundFile = sa.WaveObject.from_wave_file("./hat.wav")

# Define initial instrument notes
initial_instrument_1_notes = [
    {'instrument': 'Instrument_1', 'sample_location': './left.wav'},
]

initial_instrument_2_notes = [
    {'instrument': 'Instrument_2', 'sample_location': './right.wav'},
]

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


# Define the patterns
lists = {
    1: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],  # Odd numbers
    2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],  # Multiples of 2
    3: [2, 3, 5, 7, 11, 13, 17, 19, 2, 3],    # Prime numbers
    4: [1, 2, 4, 8, 16, 11, 1, 2, 4, 8],      # Powers of 2 mod 21
    5: [1, 3, 6, 10, 15, 1, 3, 6, 10, 15]     # Triangular numbers mod 21
}

choice = int(input("Enter your number (1-5): "))

if choice in lists:
    chosen_list = lists[choice]
    print(f"You selected: {chosen_list}")

    # Generate two lists of random values between 0.5 and 2, same length as the chosen list
    random_list1 = [random.uniform(0.5, 2) for _ in chosen_list]
    random_list2 = [random.uniform(0.5, 2) for _ in chosen_list]

    # Multiply the chosen list by both random lists and round the results to 2 decimal places
    multiplied_list1 = [round(x * r1, 2) for x, r1 in zip(chosen_list, random_list1)]
    multiplied_list2 = [round(x * r2, 2) for x, r2 in zip(chosen_list, random_list2)]

    # Calculate time intervals (in milliseconds) based on BPM
    beat_duration_ms = 60000 / bpm  # Milliseconds per beat
    time_list1 = [round(x * beat_duration_ms) for x in multiplied_list1]
    time_list2 = [round(x * beat_duration_ms) for x in multiplied_list2]

    # Create combined note list for playback with timestamps
    combined_notes = []
    for i, (t1, t2) in enumerate(zip(time_list1, time_list2)):
        combined_notes.append({'timestamp': t1 / 1000, 'duration': 0.1})  # Example duration of 0.1 seconds
        combined_notes.append({'timestamp': t2 / 1000, 'duration': 0.1})

    # Sort combined notes by timestamp (in case they're out of order)
    combined_notes.sort(key=lambda x: x['timestamp'])

    # Show the final dictionary structure
    print(f"Combined Notes (timestamps in seconds): {combined_notes}")

else:
    print("Invalid choice, please select a number between 1 and 5.")

# Store the start time
time_zero = time.time()

# Play samples based on the timestamp from the combined notes
while combined_notes:
    now = time.time() - time_zero
    ts = combined_notes[0]['timestamp']  # Check the timestamp of the next event
    duration = combined_notes[0]['duration']  # Get the duration of the note

    # Check if we passed the next timestamp,
    # if so, play sample and fetch new timestamp
    if now >= ts:
        play_obj = soundFile.play()  # Play the sound asynchronously
        time.sleep(duration)  # Sleep for the duration of the note to simulate length

        combined_notes.pop(0)  # Only pop after playing the sound and its duration

    time.sleep(0.001)  # Sleep to avoid busy waiting

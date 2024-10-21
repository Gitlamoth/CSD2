import simpleaudio as sa
import time
import random
import signal
import sys
import threading

# Load samples for two instruments
soundFile_1 = sa.WaveObject.from_wave_file("./leftleft.wav")
soundFile_2 = sa.WaveObject.from_wave_file("./rightright.wav")

# Define initial instrument notes (if needed)
initial_instrument_1_notes = [
    {'instrument': 'Instrument_1', 'sample_location': './leftleft.wav'},
]

initial_instrument_2_notes = [
    {'instrument': 'Instrument_2', 'sample_location': './rightright.wav'},
]

# Set default BPM
bpm = 100

# Define the patterns
lists = {
    1: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],  # Odd numbers
    2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],  # Multiples of 2
    3: [2, 3, 5, 7, 11, 13, 17, 19, 2, 3],    # Prime numbers
    4: [1, 2, 4, 8, 16, 11, 1, 2, 4, 8],      # Powers of 2 mod 21
    5: [1, 3, 6, 10, 15, 1, 3, 6, 10, 15]     # Triangular numbers mod 21
}

# Shared variable to store the selected list
chosen_list = lists[1]

# Signal handler to handle Ctrl+C
def signal_handler(sig, frame):
    print("\nStopping playback as Ctrl+C was pressed.")
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def generate_notes(chosen_list, bpm):
    # Generate two lists of random values between 0.5 and 2, same length as the chosen list
    random_list1 = [random.uniform(0.2, 1) for _ in chosen_list]
    random_list2 = [random.uniform(0.2, 1) for _ in chosen_list]

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
        combined_notes.append({'timestamp': t1 / 1000, 'duration': 0.1, 'instrument': 1})  # Instrument 1
        combined_notes.append({'timestamp': t2 / 1000, 'duration': 0.1, 'instrument': 2})  # Instrument 2

    # Sort combined notes by timestamp (in case they're out of order)
    combined_notes.sort(key=lambda x: x['timestamp'])

    return combined_notes

# Play the sequence based on the notes
def play_sequence():
    global chosen_list, bpm
    while True:
        combined_notes = generate_notes(chosen_list, bpm)
        time_zero = time.time()  # Store the start time

        # Play samples based on the timestamp from the combined notes
        note_index = 0  # Start from the first note
        while note_index < len(combined_notes):
            now = time.time() - time_zero
            ts = combined_notes[note_index]['timestamp']  # Check the timestamp of the next event
            duration = combined_notes[note_index]['duration']  # Get the duration of the note
            instrument = combined_notes[note_index]['instrument']  # Determine which instrument to play

            # Check if we passed the next timestamp
            if now >= ts:
                if instrument == 1:
                    play_obj = soundFile_1.play()  # Play the sound for Instrument 1
                elif instrument == 2:
                    play_obj = soundFile_2.play()  # Play the sound for Instrument 2

                time.sleep(duration)  # Sleep for the duration of the note to simulate length
                note_index += 1  # Move to the next note

            time.sleep(0.001)  # Sleep to avoid busy waiting

        # Reset the time and loop the sequence

# Thread for user input
def user_input_thread():
    global chosen_list, bpm

    while True:
        choice = int(input("Enter your number (1-5) to change the list: "))
        if choice in lists:
            chosen_list = lists[choice]
            print(f"You selected: {chosen_list}")
        else:
            print("Invalid choice, please select a number between 1 and 5.")

# Start the user input thread
input_thread = threading.Thread(target=user_input_thread, daemon=True)
input_thread.start()

# Start playing the sequence in the main thread
play_sequence()

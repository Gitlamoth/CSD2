import simpleaudio as sa
import time
import random

# Load samples for two instruments
soundFile_1 = sa.WaveObject.from_wave_file("./left.wav")
soundFile_2 = sa.WaveObject.from_wave_file("./leftleft.wav")
soundFile_3 = sa.WaveObject.from_wave_file("./right.wav")
soundFile_4 = sa.WaveObject.from_wave_file("./rightright.wav")

# Set default BPM
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

# Function to play a sequence based on the user's choice
def play_sequence(choice):
    if choice in lists:
        chosen_list = lists[choice]
        print(f"You selected: {chosen_list}")

        # Generate two lists of random values between 0.2 and 1, same length as the chosen list
        random_list1 = [random.uniform(0.66, 5) for _ in chosen_list]
        random_list2 = [random.uniform(0.66, 5) for _ in chosen_list]
        random_list3 = [random.uniform(0.66, 5) for _ in chosen_list]
        random_list4 = [random.uniform(0.66, 5) for _ in chosen_list]

        # Multiply the chosen list by both random lists and round the results to 2 decimal places
        multiplied_list1 = [round(x * r1, 2) for x, r1 in zip(chosen_list, random_list1)]
        multiplied_list2 = [round(x * r2, 2) for x, r2 in zip(chosen_list, random_list2)]
        multiplied_list3 = [round(x * r3, 2) for x, r3 in zip(chosen_list, random_list3)]
        multiplied_list4 = [round(x * r4, 2) for x, r4 in zip(chosen_list, random_list4)]

        # Calculate time intervals (in milliseconds) based on BPM
        beat_duration_ms = 60000 / bpm  # Milliseconds per beat
        time_list1 = [round(x * beat_duration_ms) for x in multiplied_list1]
        time_list2 = [round(x * beat_duration_ms) for x in multiplied_list2]
        time_list3 = [round(x * beat_duration_ms) for x in multiplied_list3]
        time_list4 = [round(x * beat_duration_ms) for x in multiplied_list4]

        # Create combined note list for playback with timestamps
        combined_notes = []
        for t1, t2, t3, t4 in zip(time_list1, time_list2, time_list3, time_list4):
            combined_notes.append({'timestamp': t1 / 1000, 'duration': 0.1, 'instrument': 1})  # Instrument 1
            combined_notes.append({'timestamp': t2 / 1000, 'duration': 0.1, 'instrument': 2})  # Instrument 2
            combined_notes.append({'timestamp': t3 / 1000, 'duration': 0.1, 'instrument': 3})  # Instrument 3
            combined_notes.append({'timestamp': t4 / 1000, 'duration': 0.1, 'instrument': 4})  # Instrument 4

        # Sort combined notes by timestamp (in case they're out of order)
        combined_notes.sort(key=lambda x: x['timestamp'])

        # Play samples based on the timestamp from the combined notes
        time_zero = time.time()  # Store the start time
        note_index = 0  # Start from the first note
        while note_index < len(combined_notes):
            now = time.time() - time_zero
            ts = combined_notes[note_index]['timestamp']  # Get the timestamp of the index
            duration = combined_notes[note_index]['duration']  # Get the duration of the note
            instrument = combined_notes[note_index]['instrument']  # Determine which instrument to play

            # Check if we passed the next timestamp
            if now >= ts:
                if instrument == 1:
                    play_obj = soundFile_1.play()  # Play the sound for Instrument 1
                elif instrument == 2:
                    play_obj = soundFile_2.play()  # Play the sound for Instrument 2
                elif instrument == 3:
                    play_obj = soundFile_3.play()  # Play the sound for Instrument 2
                elif instrument == 4:
                    play_obj = soundFile_4.play()  # Play the sound for Instrument 2

                time.sleep(duration)  # Sleep for the duration of the note to simulate length
                note_index += 1  # Move to the next index

            time.sleep(0.001)  # Sleep to avoid busy waiting

    else:
        print("Invalid choice, please select a number between 1 and 5.")

# Main loop to control the playback
while True:
    user_input = input("Enter your number (1-5) for the sequence or type 'exit' to stop: ").strip().lower()
    
    if user_input == 'exit':
        print("Stopping playback.")
        break
    
    try:
        choice = int(user_input)
        play_sequence(choice)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5 or 'exit' to stop.")

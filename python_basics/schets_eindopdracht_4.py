import simpleaudio as sa
import time
import random

# load samples for the sounds sounding
soundFile_1 = sa.WaveObject.from_wave_file("./left.wav")
soundFile_2 = sa.WaveObject.from_wave_file("./leftleft.wav")
soundFile_3 = sa.WaveObject.from_wave_file("./right.wav")
soundFile_4 = sa.WaveObject.from_wave_file("./rightright.wav")

# set default BPM
bpm = 100

# input for BPM
while True:
    user_input = input(f"Current BPM: {bpm},\nNew BPM? (or type 'no' to use default): ").strip().lower()
    
    if user_input == 'no':
        print(f"Using default BPM: {bpm}")
        break  # exit the loop and use the current bpm (default)

    try:
        bpm = int(user_input)  # try to convert input to an integer
        break  # if input is valid, break out of the loop
    except ValueError:
        print("Invalid input. Please enter a valid integer for BPM or 'no' to use the default.")

# lists to choose from
lists = {
    1: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],  # Odd numbers
    2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],  # Multiples of 2
    3: [2, 3, 5, 7, 11, 13, 17, 19, 2, 3],    # Prime numbers
    4: [1, 2, 4, 8, 16, 11, 1, 2, 4, 8],      # Powers of 2 mod 21
    5: [1, 3, 6, 10, 15, 1, 3, 6, 10, 15]     # Triangular numbers mod 21
}

# function to play a sequence based on the user's choice
def play_sequence(choice):

    if choice in lists:

        chosen_list = lists[choice]
        print(f"You selected: {chosen_list}")

        # get modulo input from the user
        while True:
            try:
                modulo_value = int(input("Enter a modulo value: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the modulo.")

        # apply the modulo operation to the chosen list
        chosen_list = [x % modulo_value for x in chosen_list]
        print(f"List after applying modulo {modulo_value}: {chosen_list}")

        # generate random lists with values between 1 and 4, matching the length of chosen_list
        # generating random values to enhance percieved symmetry as a whole in it's asymmetry
        random_list1 = [random.uniform(1, 4) for _ in range(len(chosen_list))]
        random_list2 = [random.uniform(1, 4) for _ in range(len(chosen_list))]
        random_list3 = [random.uniform(1, 4) for _ in range(len(chosen_list))]
        random_list4 = [random.uniform(1, 4) for _ in range(len(chosen_list))]

        # multiply the chosen list by the random values and round them to 3 decimal places
        multiplied_list1 = [round(x * r1, 3) for x, r1 in zip(chosen_list, random_list1)]
        multiplied_list2 = [round(x * r2, 3) for x, r2 in zip(chosen_list, random_list2)]
        multiplied_list3 = [round(x * r3, 3) for x, r3 in zip(chosen_list, random_list3)]
        multiplied_list4 = [round(x * r4, 3) for x, r4 in zip(chosen_list, random_list4)]

        # calculate time intervals based on BPM
        beat_duration_ms = 60000 / bpm 
        time_list1 = [x * beat_duration_ms for x in multiplied_list1]
        time_list2 = [x * beat_duration_ms for x in multiplied_list2]
        time_list3 = [x * beat_duration_ms for x in multiplied_list3]
        time_list4 = [x * beat_duration_ms for x in multiplied_list4]


        """
        # align the timestamps by taking the average and adjusting the individual times by ChatGPT
        # 
        aligned_time_list1, aligned_time_list2, aligned_time_list3, aligned_time_list4 = [], [], [], []
        for t1, t2, t3, t4 in zip(time_list1, time_list2, time_list3, time_list4):
            average_time = (t1 + t2 + t3 + t4) / 4  # Compute the average timestamp
            max_deviation = 0.30 * beat_duration_ms  
            aligned_time_list1.append(min(max(t1, average_time - max_deviation), average_time + max_deviation))
            aligned_time_list2.append(min(max(t2, average_time - max_deviation), average_time + max_deviation))
            aligned_time_list3.append(min(max(t3, average_time - max_deviation), average_time + max_deviation))
            aligned_time_list4.append(min(max(t4, average_time - max_deviation), average_time + max_deviation))
        """
        # Create combined note list for playback with timestamps
        combined_notes = []
        for t1, t2, t3, t4 in zip(time_list1, time_list2, time_list3, time_list4):
            combined_notes.append({'timestamp': t1 / 1000, 'duration': 0.1, 'instrument': 1})  # Instrument 1
            combined_notes.append({'timestamp': t2 / 1000, 'duration': 0.1, 'instrument': 2})  # Instrument 2
            combined_notes.append({'timestamp': t3 / 1000, 'duration': 0.1, 'instrument': 3})  # Instrument 3
            combined_notes.append({'timestamp': t4 / 1000, 'duration': 0.1, 'instrument': 4})  # Instrument 4

        # sort combined notes by timestamp by ChatGPT
        combined_notes.sort(key=lambda x: x['timestamp'])

        # play samples based on the timestamp from the combined notes
        time_zero = time.time()  # store the start time
        note_index = 0  # start from the first note
        while note_index < len(combined_notes):
            now = time.time() - time_zero
            ts = combined_notes[note_index]['timestamp']  # get the timestamp of the note
            duration = combined_notes[note_index]['duration']  # get the duration of the note
            instrument = combined_notes[note_index]['instrument']  # determine which instrument to play

            # check if we passed the next timestamp
            if now >= ts:
                if instrument == 1:
                    play_obj = soundFile_1.play()  # play the sound for instrument 1
                elif instrument == 2:
                    play_obj = soundFile_2.play()  # play the sound for instrument 2
                elif instrument == 3:
                    play_obj = soundFile_3.play()  # play the sound for instrument 3
                elif instrument == 4:
                    play_obj = soundFile_4.play()  # play the sound for instrument 4

                time.sleep(duration)  # sleep for the duration of the note to simulate length
                note_index += 1  # move to the next note

            time.sleep(0.001)  # sleep to avoid busy waiting

    else:
        print("Invalid choice, please select a number between 1 and 5.")

# main loop to control the playback
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

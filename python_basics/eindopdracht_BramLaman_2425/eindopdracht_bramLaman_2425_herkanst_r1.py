
import time
import random

# set default BPM
bpm = 100

# lists to choose from
lists = {
    1: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],  # Odd numbers
    2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],  # Multiples of 2
    3: [2, 3, 5, 7, 11, 13, 17, 19, 2, 3],    # Prime numbers
    4: [1, 2, 4, 8, 16, 11, 1, 2, 4, 8],      # Powers of 2 mod 21
    5: [1, 3, 6, 10, 15, 1, 3, 6, 10, 15]     # Triangular numbers mod 21
}



def generation (choice):
     
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

    num_lists = 4
    time_lists = []
    beat_duration_ms = 60000 / bpm 

    for index in range(num_lists):
        random_list = [random.uniform(1, 4) for index in range(len(chosen_list))]
        multiplied_list = [round(x * r1, 3) for x, r1 in zip(chosen_list, random_list)]
        print(multiplied_list)
        time_lists.append([number * beat_duration_ms for number in multiplied_list])

# Create combined note list for playback with timestamps
    combined_notes = []
    for x in zip(time_lists):
            combined_notes.append({'timestamp': x / 1000, 'duration': 0.1, 'instrument': x+1})  
            


def play_sequence(generated_lists):

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














# main loop to control the playback
while True:
    user_input = input("Enter your number (1-5) for the sequence or type 'exit' to stop: ").strip().lower()
    
    if user_input == 'exit':
        print("Stopping playback.")
        break
    
    try:
        choice = int(user_input)
        generated_lists = []
        generation(choice)
        play_sequence(generated_lists)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5 or 'exit' to stop.")


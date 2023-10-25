import simpleaudio as sa
import time
import subprocess
import multiprocessing

# added multiprocessing logic 
# to gain polyphonic playback

# Define playback function as before

def ask_samples_and_bpm():
    samples = []  # List of sample dictionaries

    try:
        bpm_input = input("Give BPM (Beats Per Minute): ")  
        # Ask for bpm
        if bpm_input == '':
            bpm = 100
            print("Current beat set to 100 BPM")
        # when no input use basis
        else:
            bpm = float(bpm_input)

    except ValueError:
        print("Invalid input for BPM. Using default BPM of 100.")
        bpm = 100
        # safety net



    while True:
        try:
            file_path = input("What sample will take place here?")
            file_path = input("now a path to that sample: ")

            # asks for list concerning length of samples in sixteenth
            event_times_str = input("what placement will the sample get in 16ths (4,3,5,4): ")
            event_times = [float(et) for et in event_times_str.split(',') if et.strip()]
            #NOTE   figure out how this extraction of list could also function
            if not event_times:
                print("No valid event times entered.")
                continue
            # safety net
            
            
            repetitions = int(input("Enter the number of times to repeat this sequence: "))
            if repetitions <= 0:
                print("Enter a positive number of repetitions.")
                continue
            # safety net
            sample_info = {
                'name': file_path,
                'file_path': file_path,
                'event_times': event_times,
                'repetitions': repetitions
            }
            
            samples.append(sample_info)  # Add the sample info to the list

            # asks for entering another sample
            another_sample = input("Add another sample? (y/n): ")
            if another_sample.lower() != 'y':
                break

            # safety net 
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    return samples, bpm # returns list of sample dictionaries and bpm

def play_sample(sample_info):
    try:
        cmd = [
            'python3',
            'poly_r5.py',
            sample_info['file_path'],
            # argument for giving file path
            ','.join(map(str, sample_info['event_times'])),
            # argument to give string of sixteenths 
            str(bpm)
        ]
        
        subprocess.run(cmd, check=True)

    except Exception as e:
        print(f"Error with playing '{sample_info['file_path']}': {e}")
        # safety net
if __name__ == "__main__":
    try:
        samples, bpm = ask_samples_and_bpm()

        processes = []

        for sample in samples:
            process = multiprocessing.Process(target=play_sample, args=(sample,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

    except KeyboardInterrupt:
        print("\nProgram stopped. (Ctrl+C)")

import simpleaudio as sa
import time
import subprocess
import multiprocessing

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
            # file_path = input("What sample will take place here?")
            # file_path = input("now a path to that sample: ")
            file_path = "/home/begligow/samples/[KB6]_Acetone_Rhythm-Ace/CLAVE.WAV"

            # asks for list concerning length of samples in sixteenth
            event_times_str = input("what placement will the sample get in 16ths (4,3,5,4): ")
            event_times = [int(et) for et in event_times_str.split(',') if et.strip()]

            #event_times = str(input("what placement will the sample get in 16ths (4,3,5,4): "))
            # event_times = [int(et) for et in event_times_input.split(',')]
            
    # event_times = ', '.join(event_times_input)
    # event_times_split = event_times_input.split(',')
    # event_times = event_times_str.split(',')
    # event_times = ', '.join(str(x) for x in my_list)
    # event_times = ', '.join(event_times_split)
            #NOTE   figure out how this extraction of list could also function
            if not event_times:
                print("No valid event times entered.")
                continue
            else: 
                print(event_times)
                
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

    return samples, bpm, repetitions# returns list of sample dictionaries and bpm



def play_sample(sample_info):


    try:


        cmd = [
            'python3',
            'poly_exp_r1.py',
            sample_info['file_path'],
            # argument for giving file path
            ','.join(map(str, sample_info['event_times'])),
            # Pass event_times as a comma-separated string
            str(bpm),
            str(repetitions),
        ]
# command creator
        
        
        subprocess.run(cmd, check=True)

    except Exception as e:
        print(f"Error with playing '{sample_info['file_path']}': {e}")
        # safety net where most errors end up
        
if __name__ == "__main__":
    
    try:
        samples, bpm, repetitions = ask_samples_and_bpm()
        
        processes = []

        for sample in samples:
            process = multiprocessing.Process(target=play_sample, args=(sample,))
            
           
            processes.append(process)
            process.start()
# --
# process = multiprocessing.Process(target=play_sample, args=(sample,)): 
#    Inside the loop, a new multiprocessing process is created 
#    using the multiprocessing module. 
#    The target is set to a function named play_sample, 
#    and the args is a tuple containing a single element, i(ndex). 
#      
# processes.append(process)
#    The created process[i] is appended to the list processes.
# process.start()
#     The start() method is called on the process to begin its execution.   
# -- 

        for process in processes:
            process.join()
# For each process, the code waits for it to 
# complete its execution by calling the join() method.
# This ensures that the main
# program waits for all subprocesses to finish before proceeding.

    except KeyboardInterrupt:
        print("\nProgram stopped. (Ctrl+C)")
 
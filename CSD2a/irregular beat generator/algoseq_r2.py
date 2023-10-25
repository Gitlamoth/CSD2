import simpleaudio as sa
import time
import subprocess
import multiprocessing
import random



def generate_rhythm(bpm, length_in_16ths):
    # Generate a simple rhythm with random hits in sizes of 16ths
    rhythm = [0]
    
    for i in range(length_in_16ths):
            
            rhythm.append(2)
            rhythm.pop(0)
            
            hit_probability = random.uniform(0, 1)
            if rhythm[0] == 0:  
                rhythm[0] +=2

            elif hit_probability > 0.50:
                rhythm.append(4)  
                rhythm[i] +=1

            elif hit_probability > 0.75:
                rhythm.append(2)
                rhythm[i] -=1

            elif hit_probability < 0.75:
                rhythm.append(2)
                rhythm[i] +=3

            else:
                rhythm.append(2)
                
    print(rhythm)
    print(sum(rhythm))
    return rhythm


def predefined_samples(bpm, length_in_16ths):
    samples = [
        {
            'file_path': "./samples/CLAVE.WAV",
            'event_times': generate_rhythm(bpm, length_in_16ths),
            'repetitions': 1
        },
        {
            'file_path': "./samples/HHCL.WAV",
            'event_times': generate_rhythm(bpm, length_in_16ths),
            'repetitions': 1
        },
        {
            'file_path': "./samples/KICK1.WAV",
            'event_times': generate_rhythm(bpm, length_in_16ths),
            'repetitions': 1
        },
        # Add more predefined samples as needed
    ]
   
    return samples






def ask_bpm_and_repetition():
   
    try:
        bpm_input = input("Give BPM (Beats Per Minute): ")
        # Ask for bpm
        if bpm_input == '':
            bpm = 100
            print("Current beat set to 100 BPM")
        # when no input use basis
        else:
            bpm = float(bpm_input)

        repetitions = int(input("Enter the number of times to repeat this sequence: "))
        # if repetitions <= 0:
        #     print("Enter a positive number of repetitions.")
        
        return bpm, repetitions  # Return all the values as a tuple
    except ValueError:
        print("Invalid input for BPM. Using default BPM of 100.")
        bpm = 100
        return bpm, repetitions  # Return all the values as a tuple
    
   


def play_sample(sample_info):


    try:


        cmd = [
            'python3',
            'algoseqsub.py',
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
            length_in_16ths = int(input("enter the step length:"))
            bpm, repetitions = ask_bpm_and_repetition()
            
            samples = predefined_samples(bpm, length_in_16ths)

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
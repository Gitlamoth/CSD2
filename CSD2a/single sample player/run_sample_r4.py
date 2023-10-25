import simpleaudio as sa
import time

def playback(sample, bpm, repetitions=1):
    try:
        # Load the Audiofile
        wave_obj = sa.WaveObject.from_wave_file(sample['file_path'])

        beat_duration = 60 / bpm / 4  # Calculate the duration of one sixteenth in seconds


        # playback forLoop in size of given repititions

        # event_time is in the size of sixteenths 
        # beat_duration gives the size of 1 sixteenth
        for _ in range(repetitions):
            for event_time in sample['event_times']:
                if event_time <= 0:
                    print(f"Error: Invalid event time for '{sample['file_path']}': {event_time}")
                    continue

                # Play Audiofile
                play_obj = wave_obj.play()
                play_obj.wait_done()

                # Sleep until it's time to play the next sample
                time.sleep(beat_duration * event_time)

    except FileNotFoundError:
        print(f"Error: Audiofile '{sample['file_path']}' couldn't be found.")
    except Exception as e:
        print(f"Error with playing '{sample['samplename']}': {e}")

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
            samplename = input("What sample will take place here?")
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
                'name': samplename,
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

def main():
    try:
        samples, bpm = ask_samples_and_bpm()

        for sample in samples:
            playback(sample, bpm, repetitions=sample['repetitions'])

    except KeyboardInterrupt:
        print("\nProgram stopped. (Ctrl+C)")

if __name__ == "__main__":
    main()

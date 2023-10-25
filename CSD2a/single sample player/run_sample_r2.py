import simpleaudio as sa
import time

def playback(Audiofile, lengths, bpm):
    try:
        # Laad het Audiofile
        wave_obj = sa.WaveObject.from_wave_file(Audiofile)

        if len(lengths) == 0:
            print("Fout: no lengths submitted for the samples.")
            return

        for length in lengths:
            if length <= 0:
                print(f"Fout: unsufficient lengths given: {length}")
                continue

            #calculates de time in seconds on basis of BPM in ratio to length being quartesnotes
            time_in_seconds = (60 / bpm) * length

            #plays Audiofile for time corresponding to current sample
            play_obj = wave_obj.play()
            play_obj.wait_done()

            # waits for playing next round in time of calculated seconds
            time.sleep(time_in_seconds)

    except FileNotFoundError:
        print(f"Fout: Audiofile '{Audiofile}' couldn't be found.")
    except Exception as e:
        print(f"error with people the Audiofile: {e}")

def ask_length_and_bpm(amount_times):
    lengths = [] # list of given lengths
    
    try:
        bpm_input = input("give BPM (Beats Per Minute): ") # Asks for bpm
        
        if bpm_input == '':
            bpm = 100
            print("Current beat set to 100 BPM")
        else:
            bpm = float(bpm_input)
    except ValueError:
        print("Invalid input for BPM. Using default BPM of 100.")
        bpm = 100

    for i in range(amount_times):
        while True:
            try:
                length = float(input(f"Give length for sample {i + 1} (quarternotes): "))
                if length <= 0:
                    print("Enter a positive input.")
                    continue

                lengths.append(length)  #   Puts given length in list lengths, the question follows up through the amount given at amount_times
                
                break
            except ValueError:
                print("Invalid input, enter a positive number.")
        
    return lengths, bpm

def main():
    try:
        Audiofile = input("Give path to Audiofile: ")
        amount_times = int(input("How many times would you like to play the sample?: "))
        lengths, bpm = ask_length_and_bpm(amount_times)
        
        playback(Audiofile, lengths, bpm)

    except KeyboardInterrupt:
        print("\nProgram stopped. (Ctrl+C)")

if __name__ == "__main__":
    main()

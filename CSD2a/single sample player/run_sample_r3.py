import simpleaudio as sa
import time

def playback(Audiofile, lengths, bpm):
    try:
        # Load the Audiofile
        wave_obj = sa.WaveObject.from_wave_file(Audiofile)

        if len(lengths) == 0:
            print("Error: No lengths submitted for the samples.")
            return

        beat_duration = 60 / bpm / 4 # Calculate the duration of one sixtienth in seconds
        current_time = time.time()

        for length in lengths:
            if length <= 0:
              print(f"Error: Insufficient length given: {length}")
              continue

            # Calculate the time to play the current sample
            play_time = current_time + beat_duration * length

            # Play Audiofile
            play_obj = wave_obj.play()
            play_obj.wait_done()

            # Sleep until it's time to play the next sample
            sleep_time = play_time - time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)

            current_time = play_time  # Update current time for the next iteration

    except FileNotFoundError:
        print(f"Error: Audiofile '{Audiofile}' couldn't be found.")
    except Exception as e:
        print(f"Error with playing the Audiofile: {e}")

def ask_length_and_bpm(amount_times):
    lengths = []  # List of given lengths

    try:
        bpm_input = input("Give BPM (Beats Per Minute): ")  # Ask for bpm

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
                length = float(input(f"Give length for sample {i + 1} (sixtienth): "))
                if length <= 0:
                    print("Enter a positive input.")
                    continue

                lengths.append(length)  # Puts given length in list lengths
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

# sample_player.py

import simpleaudio as sa
import sys #systeemwerk
import time


# event handler?
def playback(file_path, event_times, bpm, repetitions=1):
    try:
        # Load the Audiofile
        wave_obj = sa.WaveObject.from_wave_file(file_path)

        beat_duration = 60 / bpm / 4  # Calculate the duration of one sixteenth in seconds

        current_time = time.time()

        # playback forLoop in size of given repetitions
        for _ in range(repetitions):
            for event_time in event_times:
                if event_time <= 0:
                    print(f"Error: Invalid event time for '{file_path}': {event_time}")
                    continue

                # Calculate the time to play the current sample
                play_time = current_time + beat_duration * event_time

                # Play Audiofile
                play_obj = wave_obj.play()
                play_obj.wait_done()

                # Sleep until it's time to play the next sample
                sleep_time = play_time - time.time()
                if sleep_time > 0:
                    time.sleep(sleep_time)

                current_time = play_time  # Update current time for the next iteration
                time.sleep(0.001)


    except FileNotFoundError:
        print(f"Error: Audiofile '{file_path}' couldn't be found.")
    except Exception as e:
        print(f"Error with playing '{file_path}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python sample_player.py <file_path> <event_times> <bpm> <repetitions>")
        sys.exit(1)

    file_path = sys.argv[1]
    event_times = [int(et) for et in sys.argv[2].split(',')]
    bpm = float(sys.argv[3])
    repetitions = int(sys.argv[4])  #repetitions as an integer equals to the turns on the playback forLoop

    playback(file_path, event_times, bpm, repetitions)

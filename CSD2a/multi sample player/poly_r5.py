# sample_player.py

import simpleaudio as sa
import sys # systeemwerk
import time

def playback(file_path, event_times, bpm, repetitions=1):
    try:
        # Load the Audiofile
        wave_obj = sa.WaveObject.from_wave_file(file_path)

        beat_duration = 60 / bpm / 4  # Calculate the duration of one sixteenth in seconds

        for _ in range(repetitions):
            for event_time in event_times:
                if event_time <= 0:
                    print(f"Error: Invalid event time for '{file_path}': {event_time}")
                    continue

                # Play Audiofile
                play_obj = wave_obj.play()
                play_obj.wait_done()

                # Sleep until it's time to play the next sample
                time.sleep(beat_duration * event_time)

    except FileNotFoundError:
        print(f"Error: Audiofile '{file_path}' couldn't be found.")
    except Exception as e:
        print(f"Error with playing '{file_path}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python sample_player.py <file_path> <event_times> <bpm>")
        sys.exit(1)

    file_path = sys.argv[1]
    event_times = [float(et) for et in sys.argv[2].split(',')]
    bpm = float(sys.argv[3])

    playback(file_path, event_times, bpm)

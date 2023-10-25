import time
import simpleaudio as sa

# Load the audio file only once
file_path = "/home/begligow/samples/[KB6]_Acetone_Rhythm-Ace/CLAVE.WAV"
wave_obj = sa.WaveObject.from_wave_file(file_path)

# Rhythmic sequence in quarter notes and BPM
note_dur_seq = [4, 1, 6, 4, 2, 5, 4]
bpm = 128

# Calculate the duration of one sixteenth in seconds
beat_duration = 60 / bpm / 4

# Store the current time
time_zero = time.time()

# Define playback function with deviation correction
def playback(file_path, event_time, last_deviation):
    wave_obj = sa.WaveObject.from_wave_file(file_path)

    if event_time < 0:
        event_time = 0  # Ensure event_time is not negative

    # Play Audiofile and measure playback time
    play_obj = wave_obj.play()
    play_start_time = time.time()
    play_obj.wait_done()
    play_end_time = time.time()

    # Calculate the actual playback time
    actual_playback_time = play_end_time - play_start_time

    # Calculate the deviation in seconds
    current_deviation = (time.time() - time_zero - event_time) / 1000.0
    deviation = current_deviation - last_deviation
    adjusted_sleep_time = (beat_duration * (event_time + deviation)) - actual_playback_time

    if adjusted_sleep_time > 0:
        time.sleep(adjusted_sleep_time)

    # Print the deviation in seconds
    print(f"Deviation: {deviation:.3f} s")

    return current_deviation

def main_loop():
    last_deviation = 0

    for note_dur in note_dur_seq:
        last_deviation = playback(file_path, note_dur, last_deviation)

# Set the number of loops you want
num_loops = 15  # Change this to the number of loops you desire

loop_count = 0

# Run the main loop for the specified number of times
while loop_count < num_loops:
    main_loop()
    loop_count += 1

print("Finished all loops.")

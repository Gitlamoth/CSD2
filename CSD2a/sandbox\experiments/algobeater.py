import time
import simpleaudio as sa

# Function to calculate time intervals based on user input
def calculate_intervals(bpm, *multipliers):
    intervals = [(60 / (bpm * int(multiplier))) for multiplier in multipliers]
    return intervals




# Store the current time
time_zero = time.time()

# Function to play a sample with deviation correction
def playback(sample, event_time, bpm, last_deviation):
    wave_obj = sa.WaveObject.from_wave_file(sample)
    beat_duration = 60 / bpm 
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
    current_deviation = (time.time() - start_time - event_time) / 1000.0
    deviation = current_deviation - last_deviation
    adjusted_sleep_time = (beat_duration * event_time) - actual_playback_time - deviation

    if adjusted_sleep_time > 0:
        time.sleep(adjusted_sleep_time)

    # Print the deviation in seconds
    print(f"Deviation: {deviation:.3f} s")
    print(intervals)
    return deviation

# Get user input for BPM
bpm = int(input("Enter BPM: "))

# Get user input for multipliers
multipliers = input("Enter multipliers separated by commas (e.g., 6,2,1): ").split(',')

# Calculate time intervals based on user input
intervals = calculate_intervals(bpm, *multipliers)

# Sample to play
sample = "/home/begligow/samples/[KB6]_Acetone_Rhythm-Ace/CLAVE.WAV"

# Store the start time
start_time = time.time()

# Initialize deviation
deviation = 0

# Set the number of loops you want
num_loops = 15  # Change this to the number of loops you desire

loop_count = 0

while loop_count < num_loops:
    for interval in intervals:
        playback(sample, interval, bpm, deviation)

    loop_count += 1
    
    
    
# except KeyboardInterrupt:
#     print("\nProgram stopped. (Ctrl+C)")

print("Finished playback.")

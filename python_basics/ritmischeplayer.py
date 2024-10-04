import simpleaudio as sa
import time

#loadsample
soundFile = sa.WaveObject.from_wave_file("./hat.wav")

#how many times the sample has to be repeated
events = int(input("how many events? "))
event_durations = list()


#asks for durations amount for an event
#this fills a list 'event_durations'
#as many times as it's given for variable 'events'
for i in range(int(events)):
    event_durations.append(float(input("Enter event duration\n")))


#this prints the list of given event durations
print("note_durations:", event_durations)


#asks user for bpm
bpm = float(input("Enter BPM\n"))



#how much the value will be of one quarternote corresponding to the bpm
quarternote_dur = 60.0 / bpm
print("bpm:", bpm, "quarternote_dur", quarternote_dur)


# turns event durations to list of time durations (sec)
# 
time_durations = []

for time_dur in event_durations:
    time_durations.append(quarternote_dur * time_dur)

#play sequence
for eventinterval in time_durations:

    play_obj = soundFile.play()
    time.sleep(eventinterval)
    time.sleep(0.001)


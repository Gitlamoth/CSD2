import simpleaudio as sa
import time

#how many times the sample has to be repeated
times = int(input("how many times? "))
#bpm for now
bpm = int(input("please enter bpm ~100/200:"))

#loadsample
soundFile = sa.WaveObject.from_wave_file("./hat.wav")

note_durs = []
time_durs = []

for p in range(number_of_repeats):
    play_obj


import simpleaudio as sa
import time
times = int(input("how many times? "))

soundFile = sa.WaveObject.from_wave_file("./hat.wav")

for x in range(times):
    
    play_obj = soundFile.play()
    time.sleep(0.5)
       

play_obj.wait_done()



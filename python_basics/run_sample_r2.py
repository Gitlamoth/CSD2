import simpleaudio as sa
import time

def afspelen(Audiofile, lengths, bpm):
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

            # Bereken de tijd in seconden op basis van de BPM en de verhouding
            time_in_seconds = (60 / bpm) * length

            # Speel het Audiofile af voor de berekende tijd
            play_obj = wave_obj.play()
            play_obj.wait_done()

            # Wacht tot de duur van de noot en de vertraging voor de volgende sample
            time.sleep(time_in_seconds)

    except FileNotFoundError:
        print(f"Fout: Audiofile '{Audiofile}' kon niet worden gevonden.")
    except Exception as e:
        print(f"Fout bij het afspelen van het Audiofile: {e}")

def ask_length_and_bpm(amount_times):
    lengths = [] # list of given lengths
    bpm = float(input("Geef het BPM (Beats Per Minute): ")) # Asks for bpm
    

    for i in range(amount_times):
        while True:
            try:
                length = float(input(f"Geef de length voor sample {i + 1} (kwartnoten): "))
                if length <= 0:
                    print("Voer een positieve length in.")
                    continue

                lengths.append(length)  #   Puts given length in list lengths, the question follows up through the amount given at amount_times
                
                break
            except ValueError: print("Ongeldige invoer. Voer een positieve length in.")
    
    return lengths, bpm

def main():
    try:
       
        Audiofile = input("Geef het pad naar het Audiofile (bijv. sample.wav): ")
        amount_times = int(input("How many times would you like to play the sample?"))
        lengths, bpm = ask_length_and_bpm(amount_times)

        
        
        afspelen(Audiofile, lengths, bpm)


    except KeyboardInterrupt:
        print("\nProgram stopped. (Ctrl+C)")


if __name__ == "__main__":
    main()

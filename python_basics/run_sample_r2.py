import simpleaudio as sa
import time

def afspelen(audiobestand, lengtes, bpm):
    try:
        # Laad het audiobestand
        wave_obj = sa.WaveObject.from_wave_file(audiobestand)

        if len(lengtes) == 0:
            print("Fout: Geen lengtes opgegeven voor de samples.")
            return

        for lengte in lengtes:
            if lengte <= 0:
                print(f"Fout: Ongeldige lengte opgegeven: {lengte}")
                continue

            # Bereken de tijd in seconden op basis van de BPM en de verhouding
            tijd_in_seconden = (60 / bpm) * lengte

            # Speel het audiobestand af voor de berekende tijd
            play_obj = wave_obj.play()
            play_obj.wait_done()

            # Wacht tot de duur van de noot en de vertraging voor de volgende sample
            time.sleep(tijd_in_seconden)

    except FileNotFoundError:
        print(f"Fout: Audiobestand '{audiobestand}' kon niet worden gevonden.")
    except Exception as e:
        print(f"Fout bij het afspelen van het audiobestand: {e}")

def vraag_lengtes_bpm(aantal_keer):
    lengtes = []
    bpm = float(input("Geef het BPM (Beats Per Minute): "))
    for i in range(aantal_keer):
        while True:
            try:
                lengte = float(input(f"Geef de lengte voor sample {i + 1} (kwartnoten): "))
                if lengte <= 0:
                    print("Voer een positieve lengte in.")
                    continue
                lengtes.append(lengte)
                break
            except ValueError:
                print("Ongeldige invoer. Voer een positieve lengte in.")
    return lengtes, bpm

def main():
    try:
        audiobestand = input("Geef het pad naar het audiobestand (bijv. sample.wav): ")
        
        aantal_keer = int(input("Hoe vaak wil je de sample afspelen? "))
        lengtes, bpm = vraag_lengtes_bpm(aantal_keer)
        
        afspelen(audiobestand, lengtes, bpm)
    except KeyboardInterrupt:
        print("\nProgramma gestopt. (Ctrl+C)")

if __name__ == "__main__":
    main()

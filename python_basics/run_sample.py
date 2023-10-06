import simpleaudio as sa

def afspelen(audiobestand, aantal_keer):
    try:
        # Laad het audiobestand
        wave_obj = sa.WaveObject.from_wave_file(audiobestand)
        
        for _ in range(aantal_keer):
            # Speel het audiobestand af
            play_obj = wave_obj.play()
            play_obj.wait_done()
    except FileNotFoundError:
        print(f"Fout: Audiobestand '{audiobestand}' kon niet worden gevonden.")
    except Exception as e:
        print(f"Fout bij het afspelen van het audiobestand: {e}")

def vraag_aantal_keer():
    while True:
        try:
            aantal_keer = int(input("Hoe vaak wil je de sample afspelen? "))
            if aantal_keer <= 0:
                print("Voer een positief geheel getal in.")
                continue
            return aantal_keer
        except ValueError:
            print("Ongeldige invoer. Voer een positief geheel getal in.")

def main():
    try:
        audiobestand = input("Geef het pad naar het audiobestand (bijv. sample.wav): ")
        
        aantal_keer = vraag_aantal_keer()
        
        afspelen(audiobestand, aantal_keer)
    except KeyboardInterrupt:
        print("\nProgramma gestopt. (Ctrl+C)")

if __name__ == "__main__":
    main()

def fill_measure_with_events(measures):
    events = []
    
    for measure in range(int(measures)):
        # Initialize a list of 16 slots for the current measure
        measure_events = [0] * 16
        current_index = 0

        # Continue to prompt the user until the measure is filled
        while current_index < 16:
            remaining_sixteenths = 16 - current_index
            event_duration = int(input(f"Enter event duration in sixteenths (remaining: {remaining_sixteenths})\nStarting at sixteenth {current_index + 1}: "))

            if event_duration > remaining_sixteenths:
                print(f"Error: Event duration exceeds remaining sixteenth notes. Try again.")
            else:
                # Fill in the current event duration in the measure
                for i in range(event_duration):
                    measure_events[current_index + i] = 1  # Mark this slot as filled

                # Move the current index to the next available position
                current_index += event_duration

        events.append(measure_events)

    return events

# Example usage:
num_measures = input("How many measures do you want to fill? ")
filled_events = fill_measure_with_events(num_measures)

print("Filled events for each measure:")
for i, measure in enumerate(filled_events):
    print(f"Measure {i + 1}: {measure}")

import sys

note = input("Enter a note (e.g., c, F#, etc.): ").capitalize()
print("Note Selected: ", note)

all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F',
             'F#', 'G', 'G#', 'A', 'A#', 'B']
flat_map = {
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#",
    "Bb": "A#"
}

if note not in flat_map and note not in all_notes:
    print("Not a valid note: ", note)
    sys.exit(1)

# Major scale formula: 2 = whole step, 1 = half step
major_scale = [2,2,1,2,2,2,1]

# We need to loop through all notes from index of (root note) note
# print root note
# Add the major scale formula to index pointer, mod 12 to loop back to tonic/root (just incase)
# Account for validating user input for only natural notes
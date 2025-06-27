import sys

note = input("Enter a note (e.g., c, F#, etc.): ").capitalize()
print("Note Selected: ", note)

all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F',
             'F#', 'G', 'G#', 'A', 'A#', 'B']

indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

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
major_scale_steps = [2,2,1,2,2,2,1]

# We need to loop through all notes from index of (root note) note
# print root note
# Add the major scale formula to index pointer, mod 12 to loop back to tonic/root (just incase)
# Account for validating user input for only natural notes
# Major scale loop through each major scale step and add to root index

rootIndex = all_notes.index(note)
print(all_notes[rootIndex])

for major_scale_step in major_scale_steps:
    rootIndex += major_scale_step
    if rootIndex > len(all_notes) - 1:
        rootIndex %= 12
    print(all_notes[rootIndex])



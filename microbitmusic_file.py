import music

music.play(music.NYAN)

import music

tune = ["A4:4", "C5:4", "G5:4", "F5:4", "A4:4", "A4:2", "G4:2", "A4:2", "Bb4:4"]

music.play(tune)

import music

tune = ["A4:3", "C5:3", "G5:3", "F5:3", "A4:3", "A4:3", "G4:2", "A4:2", "Bb4:4", "A0:3", "A4:3", "C5:3", "G5:3", "F5:3", "A4:3", "A4:3", "G4:2", "A4:2", "Bb4:4",
"A0:3", "C5:5", "F4:3", "A4:2", "Bb4:2", "C5:2", "C5:4", "Bb4:2", "A4:2", "G4:1", "F4:2", "A4:3", "G4:2", "A0:2",
"A4:2", "G4:2", "F4:2", "F4:1", "G4:1", "F4:1", "A0:2", "F4:7"]

music.play(tune)

import music

while True:
    for freq in range(880, 1760, 16):
        music.pitch(freq, 6)
    for freq in range(1760, 880, -16):
        music.pitch(freq, 6)


from music21 import note,stream,corpus,chord,environment,converter,midi

stream1 = stream.Stream()
note = note.Note("C4", quarterLength = 1)
stream1.repeatAppend(note, 4)
stream1.show()

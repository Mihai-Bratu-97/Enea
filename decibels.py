from scipy.io import wavfile
from Audio_recording import recording_audio
import math

def get_dbs(wav):
    samplerate, data = wavfile.read(wav) # I extracted samplerate and data from audio file
    square = 0 # from line 8 till line 13, I used a math formula that computes rms, which I'll use later for computing the number of db
    n = len(data)
    for i in range(0, n):
        square += int(data[i])**2
    mean = square / n
    root = math.sqrt(mean)
    lvl_of_db = 20 * math.log10(root) # I computed the number of decibels using another math formula
    f = open("level_of_db.txt", "a") # I opened a text file, whose name is level_of_db.txt
    f.write("The level of db is: " + str(lvl_of_db) + '\n') # I wrote the number of db in that file
    f.close() # I closed the file

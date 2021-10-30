from scipy.io import wavfile
import math

def initialise_data(wav):
    samplerate, data = wavfile.read(wav) # I extracted samplerate and data from audio file
    return data

def rms_calcul(data):
    square = 0
    n = len(data)
    for i in range(0, n):
        square += int(data[i])**2
    mean = square / n
    root = math.sqrt(mean)
    return root

def dbs_calcul(root):
    lvl_of_dbs = 20 * math.log10(root) # I computed the number of decibels using another math formula
    print("The level of dbs has succesfully computed")
    return lvl_of_dbs

def writing_number_of_dbs(lvl_of_dbs):
    f = open("level_of_db.txt", "a") # I opened a text file, whose name is level_of_db.txt
    f.write("The level of db is: " + str(lvl_of_dbs) + '\n') # I wrote the number of db in that file
    f.close() # I closed the file

def get_dbs():
    data_list = initialise_data("recorded.wav")
    rms = rms_calcul(data_list)
    dbs = dbs_calcul(rms)
    written_dbs = writing_number_of_dbs(dbs)

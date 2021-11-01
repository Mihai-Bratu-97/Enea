from scipy.io import wavfile
import math

class DbsScript:
        def __init__(self, wav):
        try:
            self.samplerate, self.data = wavfile.read(wav) # extracts the samplerate(44100), and the data, as a list with numbers
            self.written_file()
        except:
            print("No audio file found! So the number of dbs couldn't be computed!")

    # this function computes the rms(root mean square)
    def calcul_rms(self):
        square = 0
        n = len(self.data)
        for i in range(0, n):
            square += int(self.data[i]) ** 2
        mean = square / n
        root = math.sqrt(mean)
        return root

    # this function computes the number of decibels, based on a math formula
    def dbs_number(self):
        lvl_of_dbs = 20 * math.log10(self.calcul_rms())
        print("The lvl of dbs has been successfully computed!")
        return lvl_of_dbs

    # this function writes the number of dbs into a file
    def written_file(self):
        f = open("level_of_dbs.txt", "a")  # I opened a text file, whose name is level_of_dbs.txt
        f.write("The level of dbs is: " + str(self.dbs_number()) + '\n')  # I wrote the number of db in that file
        f.close()  # I closed the file

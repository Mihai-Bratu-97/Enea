from scipy.io import wavfile
import math

class DbsScript:
    def __init__(self, wav):
        self.samplerate, self.data = wavfile.read(wav)
        self.written_file()

    def calcul_rms(self):
        square = 0
        n = len(self.data)
        for i in range(0, n):
            square += int(self.data[i]) ** 2
        mean = square / n
        root = math.sqrt(mean)
        return root

    def dbs_number(self):
        lvl_of_dbs = 20 * math.log10(self.calcul_rms())
        print("The lvl of dbs has been successfully computed!")
        return lvl_of_dbs

    def written_file(self):
        f = open("level_of_dbs.txt", "a")  # I opened a text file, whose name is level_of_dbs.txt
        f.write("The level of dbs is: " + str(self.dbs_number()) + '\n')  # I wrote the number of db in that file
        f.close()  # I closed the file
import pyaudio
import wave

class AudioScript:
    def __init__(self):
        self.filename = "recorded.wav" # the name of the file
        self.chunk = 1024 # set the chunk size of 1024 samples
        self.FORMAT = pyaudio.paInt16 # sample format
        self.channels = 1 # mono
        self.sample_rate = 44100 # 44100 samples per second
        self.record_seconds = 121
        self.starting_recording(self.record_seconds)

    # this function starts the recording
    def starting_recording(self, record_seconds):
        try:
            p = pyaudio.PyAudio() # initialize PyAudio object
            stream = p.open(format=self.FORMAT,
                            channels=self.channels,
                            rate=self.sample_rate,
                            input=True,
                            output=True,
                            frames_per_buffer=self.chunk) # open stream object as input & output
            frames = []
            count = 0
            print("Starts audio recording")
            for i in range(int(44100 / self.chunk * record_seconds)):
                if count % 43 == 0:
                    print("Audio recording...")
                count += 1
                data = stream.read(self.chunk)
                frames.append(data)
            print("Audio recording has finished!")
            # stop and close stream
            stream.stop_stream()
            stream.close()
            # terminate pyaudio object
            p.terminate()
            # save audio file
            # open the file in 'write bytes' mode
            wf = wave.open(self.filename, "wb")
            # set the channels
            wf.setnchannels(self.channels)
            # set the sample format
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            # set the sample rate
            wf.setframerate(self.sample_rate)
            # write the frames as bytes
            wf.writeframes(b"".join(frames))
            # close the file
            wf.close()
        except:
            print("No microphone detected! Check it and run the script again!")

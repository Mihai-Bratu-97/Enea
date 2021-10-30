import pyaudio
import wave

class AudioScript:
    def __init__(self):
        self.filename = "recorded.wav"
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 44100
        self.record_seconds = 11 # 120
        self.starting_recording(self.record_seconds)

    def starting_recording(self, record_seconds):
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=self.FORMAT,
                            channels=self.channels,
                            rate=self.sample_rate,
                            input=True,
                            output=True,
                            frames_per_buffer=self.chunk)
            frames = []
            count = 0
            print("Starting audio recording")
            for i in range(int(44100 / self.chunk * record_seconds)):
                if count % 43 == 0:
                    print("Audio recording...")
                count += 1
                data = stream.read(self.chunk)
                frames.append(data)

            # stop and close stream
            print("Finishing audio recording!")
            stream.stop_stream()
            stream.close()
            p.terminate()
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
            print("No microphone detected!")
            return None
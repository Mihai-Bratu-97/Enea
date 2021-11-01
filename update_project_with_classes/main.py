from youtube_scraping import YoutubeScript
from Video_recording import VideoScript
from Audio_recording import AudioScript
from decibels import DbsScript
from threading import Thread
import time

if __name__ == "__main__":
    youtube = Thread(target=YoutubeScript)
    video = Thread(target=VideoScript)
    audio = Thread(target=AudioScript)
    decibels = Thread(target=DbsScript, args=["recorded.wav"])
    youtube.start()
    youtube.join()
    audio.start()
    time.sleep(0.3)
    if audio.is_alive():
        video.start()
        video.join()
        audio.join()
        decibels.start()

from youtube_scraping import YoutubeScript
from Video_recording import VideoScript
from Audio_recording import AudioScript
from decibels import DbsScript
import threading
from threading import Thread
def main():
    youtube = Thread(target=YoutubeScript)
    video = Thread(target=VideoScript)
    audio = Thread(target=AudioScript)
    decibels = Thread(target=DbsScript, args=["recorded.wav"])
    youtube.start()
    youtube.join()
    audio.start()
    video.start()
    video.join()
    audio.join()
    decibels.start()

main()

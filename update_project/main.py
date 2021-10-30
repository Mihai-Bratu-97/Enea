from Youtube_random_video import youtube_script
from Video_recording import video_recording_script
from Audio_recording import audio_recording_script
from decibels import dbs_script
from threading import Thread

def main():
    youtube = Thread(target = youtube_script)
    video = Thread(target = video_recording_script)
    audio = Thread(target = audio_recording_script)
    decibels = Thread(target = dbs_script)
    youtube.start()
    youtube.join()
    audio.start()
    video.start()
    video.join()
    audio.join()
    decibels.start()

main()
import os
import pytube
from pytube.cli import on_progress

# Kullanıcıdan video bağlantısını ve indirme formatını al
url = input("Lütfen bir YouTube video bağlantısı girin: ")
format = input("Hangi formatta indirmek istersiniz? (mp3/mp4): ")

# İndirme dizini oluştur
directory = "downloads"
if not os.path.exists(directory):
    os.makedirs(directory)

# Videoyu indir
yt = pytube.YouTube(url, on_progress_callback=on_progress)
if format == "mp3":
    video = yt.streams.filter(only_audio=True).first()
    extension = "mp3"
else:
    video = yt.streams.get_highest_resolution()
    extension = "mp4"


# İndirme işlemini başlat
video.download(directory, filename=yt.title)
if format == "mp3":
    # Videoyu mp3'e dönüştür
    video_file = os.path.join(directory, f"{yt.title}.{extension}")
    audio_file = os.path.join(directory, f"{yt.title}.mp3")
    os.system(f"ffmpeg -i {video_file} {audio_file}")
    os.remove(video_file)

print("İndirme tamamlandı!")
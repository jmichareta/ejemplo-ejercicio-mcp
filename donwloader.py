import yt_dlp

url = input("Introduce la URL del video de YouTube: ")
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

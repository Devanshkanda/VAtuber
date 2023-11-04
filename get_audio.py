from pytube import YouTube

def download_audio(url: str):
    try:
        yt = YouTube(url=url)
        audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4")
        audio_stream.download()
        print("audio downloaded successfully")
    except Exception as e:
        print("An error occured" + str(e))


if __name__ == "__main__":

    urli = input("Enter the URL of the Video : ")
    download_audio(urli)

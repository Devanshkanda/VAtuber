from pytube import YouTube
import argparse

def download_audio(url: str, type: str, filename: str):
    try:
        yt = YouTube(url=url)
        audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4").first()
        # print(audio_stream)
        if(audio_stream is None):
            return "No file format is available"
        
        print("Downloading the file. please wait for few Seconds")

        if not filename:
            audio_stream.download()
        else:
            audio_stream.download(filename=f"{filename}.mp3")

        print(f"{type} downloaded successfully")
    except Exception as e:
        print("An error occured : " + str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Welcome Here to convert your
                                    favourate video to audio...""")
    
    parser.add_argument("--url", type=str, help="Enter the Url of the youtube video here")
    parser.add_argument("--type", type=str, help="Enter the Type format of the file (audio/video)")
    parser.add_argument("--name", type=str, help="Enter the name of file without .ext Example : 'audio' ", default="")

    args = parser.parse_args()

    url = args.url
    filetype = args.type
    name = args.name

    if(args.url is None):
            print("Enter the url .")
            quit()
    elif(filetype == "audio" or filetype == "video" and url):
        download_audio(url, filetype, name)
    else:
        print("Please enter the correct input format")
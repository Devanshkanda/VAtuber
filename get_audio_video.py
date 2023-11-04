from pytube import YouTube
import argparse


def download_audio(url: str, type: str, filename: str):
    try:
        yt = YouTube(url=url)
        audio_stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4", type="audio").first()
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


def download_video(url: str, type: str, filename: str, res: str):
    try:
        yt = YouTube(url=url)
        video_stream = yt.streams.filter(only_video=True, mime_type="video/mp4", type="video", res=res).first()
        # print(video_stream)
        if(video_stream is None):
            return "No file format is available"
        
        print("Downloading the file. please wait for few Seconds ...")

        if not filename:
            video_stream.download()
        else:
            video_stream.download(filename=f"{filename}.mp4")

        print(f"{type} downloaded successfully")
    except Exception as e:
        print("An error occured : " + str(e))


def create_arge_parser():
    parser = argparse.ArgumentParser(description="""Welcome Here to convert your
                                    favourate video to audio...""")
    
    parser.add_argument("--url", type=str, help="Enter the Url of the youtube video here")
    parser.add_argument("--type", type=str, help="Enter the Type format of the file (audio/video)")
    parser.add_argument("--name", type=str, help="Enter the name of file without .ext Example : 'audio' ", default="")
    parser.add_argument("--res", type=str, help="Enter the resolution type when downloading video Example: '1080p'. Default set to 480p", default="480p")

    return parser.parse_args()


if __name__ == "__main__":
    args = create_arge_parser()
    url = args.url
    filetype = args.type
    name = args.name
    res = args.res

    if(url is None or not url):
        print("Enter the url .")
        quit()
    elif(filetype == "audio" and url):
        download_audio(url, filetype, name)
    elif(filetype == "video" and url):
        download_video(url, filetype, name, res)
    else:
        print("Please enter the correct input format")

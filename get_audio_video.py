from pytube import YouTube
import argparse
from pathlib import Path


class customException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return self.message


class get_StreamFile:

    def download_file(self, url: str, type: str, filename: str, res: str) -> None:
        try:
            yt = YouTube(url=url)
            stream = None
            extension: str;

            if type == "audio":
                stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4", type="audio").first()
                extension = "mp3"

                if(stream is None):
                    raise customException("No file format Stream is available")
                
            elif type == "video":
                stream = yt.streams.filter(only_video=True, mime_type="video/mp4", type="video", res=res).first()
                extension = "mp4"

                if(stream is None):
                    raise customException("No file format Stream is available")
                
            else:
                raise customException("Unknown file type entered ..")

            print("Downloading the file. please wait for few Seconds ...")

            if not filename:
                stream.download()
            else:
                stream.download(filename=f"{filename}.{extension}")

            print(f"{type} downloaded successfully at Path: {Path.cwd()}")

        except customException as e:
            print(f"An error occured: {str(e)}")
        except Exception as e:
            print(f"An error occured: {str(e)}")


    def create_arge_parser(self):
        parser = argparse.ArgumentParser(description="""Welcome Here to convert your
                                        favourate video to audio...""")
        
        parser.add_argument("--url", type=str, help="Enter the Url of the youtube video here", default=None)
        parser.add_argument("--type", type=str, help="Enter the Type format of the file (audio/video)")
        parser.add_argument("--name", type=str, help="Enter the name of file without .ext Example : 'audio' ", default="")
        parser.add_argument("--res", type=str, help="Enter the resolution type when downloading video Example: '1080p'. Default set to 480p", default="480p")

        return parser.parse_args()


if __name__ == "__main__":

    obj = get_StreamFile()
    args = obj.create_arge_parser()
    url: str = args.url
    filetype: str = args.type
    name: str = args.name
    res: str = args.res

    if(url is None or not url):
        print("Enter the url .")
        quit()
    elif(filetype == "audio" and url) or (filetype == "video" and url):
        obj.download_file(url=url, type=filetype, filename=name, res=res)
    else:
        print("Please enter the correct input format")

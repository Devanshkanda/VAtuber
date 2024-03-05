from pytube import YouTube
import argparse, threading, asyncio, time
from pathlib import Path
from pytube.cli import on_progress


class customException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    @property
    def __str__(self) -> str:
        return self.message


class get_StreamFile:

    def __init__(self, url: list, type: str, filename: str, res: str) -> None:
        self.urls: list = url
        self.type: str = type
        self.filename: str = filename
        self.res: str = res


    def download_file(self, url: str) -> None:
        try:
            yt = YouTube(url=url, on_progress_callback=on_progress)
            stream = None
            extension: str

            if self.type == "audio":
                stream = yt.streams.filter(only_audio=True, mime_type="audio/mp4", type="audio").first()
                extension = "mp3"

                if(stream is None):
                    raise customException("No file format Stream is available")
                
            elif self.type == "video":
                stream = yt.streams.filter(only_video=True, mime_type="video/mp4", type="video", res=self.res).first()
                extension = "mp4"

                if(stream is None):
                    raise customException("No file format Stream is available")
                
            else:
                raise customException("Unknown file type entered ..")
                # quit()

            print("Downloading the file. please wait for few Seconds ...")
            print(f"Title: {stream.title}")
            print(f"filesize: {stream.filesize/(1024*1024)} MB")

            if not self.filename:
                stream.download()
            else:
                stream.download(filename=f"{self.filename}.{extension}")

            print(f"{self.type} downloaded successfully at Path: {Path.cwd()}/{stream.title}\n")

        except customException as e:
            print(f"An error occured: {str(e)}")
        except Exception as e:
            print(f"An error occured: {str(e)}")


    @staticmethod
    def create_arge_parser():
        parser = argparse.ArgumentParser(description="""Welcome Here to convert your
                                        favourate video to audio...""")
        
        parser.add_argument("--url", nargs='*', help="Enter the Url(s) of the youtube video here", default=None)
        parser.add_argument("--type", type=str, help="Enter the Type format of the file (audio/video)", default=None)
        parser.add_argument("--name", type=str, help="Enter the name of file without .ext Example : 'audio' ", default="")
        parser.add_argument("--res", type=str, help="Enter the resolution type when downloading video Example: '1080p'. Default set to 480p", default="480p")

        return parser.parse_args()
    
    
    async def start_download(self) -> None:
        for url in self.urls:
            threading.Thread(target=self.download_file, args=(url,)).start()


async def main() -> None:
    args = get_StreamFile.create_arge_parser()
    url: list = args.url
    filetype: str = args.type
    name: str = args.name
    res: str = args.res

    if(url is None or not url):
        print("Enter the url .")
        quit()
    elif(filetype == "audio" and url) or (filetype == "video" and url):
        get_streamFile_obj = get_StreamFile(url=url, type=filetype, filename=name, res=res)
        await get_streamFile_obj.start_download()
    else:
        print("Please enter the correct input format")


if __name__ == "__main__":
    asyncio.run(main())
#!/usr/bin/python3


from pytube import YouTube
from argparse import ArgumentParser

parser = ArgumentParser(description="Youtube Video downloader",epilog="[ Usage ] : python3 tubedown.py -u https://youtu.be/xxxxxxx")
parser.add_argument('-u','--url',dest="link",metavar='',help="Youtube video link",required=True)
args = parser.parse_args()

def banner():
    print("*" * 120)
    print("""
██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ 
██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
██║   ██║   ██║   ██║   ██║██████╔╝█████╗█████╗██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║
██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝╚════╝██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║
╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝
 ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝                                                                                                
""")
    print("""                                                   By @yuvarajucet [ Mr_3rr0r_501 ]                                                                                                                """)
    print("*" * 120)

def download():
    try:
        yt = YouTube(args.link)
    except KeyboardInterrupt:
        print("#" * 50)
        print("⌨️ You pressed [Ctrl + C ] ⌨️")
        print("#" * 50)
        exit(1)

    except Exception:
        print("#" * 50)
        print("😭  Connection Error Kindly check your URL. 😭")
        print("#" * 50)
        exit(1)


    re_video = yt.streams.get_highest_resolution()
    try:
        print("-" * 50)
        print("📥  Video Downloading... 📥")
        print("-" * 50)
        re_video.download()
    except:
        print("#" * 50)
        print("👎 Some error accured! 👎")
        print("#" * 50)
        exit(1)
    print("❤️" * 50)
    print("🥳  Download Completed!  👍")
    print("❤️" * 50)

if __name__ == "__main__":
    banner()
    download()

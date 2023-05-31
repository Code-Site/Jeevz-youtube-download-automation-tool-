#!python3
import downloader
from downloader import downloader_single
from downloader import downloader_playlist

run = True

while run:
    Ask_user = input("[+] Playlist[p] or Single[s]:")

    if Ask_user.strip() == 'p':
        print("Caution! Can only accept playlist with videos under 60 secs")
        get_playlist_link = input("[+] Enter playlist link:")
        downloader_playlist(get_playlist_link.strip())

    elif Ask_user.strip() == 's':
        print("Caution! Can only accept videos under 60 secs")
        get_link = input("[+] Enter video link: ")
        downloader_single(get_link.strip())
              
    else:
        print("command not found.. try again")

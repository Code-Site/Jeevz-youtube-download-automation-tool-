import pytube, re
from pytube import YouTube
from pytube import Playlist

def downloader_single(link):
    yt = YouTube(link)
    print("Starting...")
    print("getting streams...")
    
    streams = yt.streams

    print("filtering streams...")
    

    filtered_streams = []
    for stream in streams:
        if stream.mime_type == "video/mp4" and stream.resolution == "720p" and stream.is_progressive == True:
            filtered_streams.append(stream)

    if len(filtered_streams) == 1:
        select_stream = filtered_streams[0]
        get_itag = select_stream.itag
    elif len(filtered_stream) > 1:
        select_stream = filtered_streams[0]
        get_itag = select_stream.itag

    download_stream = yt.streams.get_by_itag(get_itag)

    print("Downloading stream...")

    download_stream.download(output_path = r"C:\Users\Jeevan\Desktop\Personal\Personal projects\Youtube Automation AI\Downloaded_videos")

    print(f"Download completed for '{yt.title}'")

def downloader_playlist(playlist_link):
    print("Starting...")
    playlist_link = Playlist(playlist_link)

    counter = 0
    playlist_list = []
    
    for lenny in playlist_link.video_urls:
        playlist_list.append(lenny)

    print(f"The playlist has {len(playlist_list)} videos")
    
    start_range = int(input("Start Range:")) 
    stop_range = int(input("Stop Range:"))
    
    for url in range(start_range - 1, stop_range):
        yt = YouTube(playlist_list[url])
        streams = yt.streams
        filtered_streams = []
        
        print("filtering streams...")
        for stream in streams:
            if stream.mime_type == "video/mp4" and stream.resolution == "720p" and stream.is_progressive == True:
                filtered_streams.append(stream)

        if len(filtered_streams) == 1:
            select_stream = filtered_streams[0]
            get_itag = select_stream.itag
        elif len(filtered_stream) > 1:
            select_stream = filtered_streams[0]
            get_itag = select_stream.itag

        download_stream = yt.streams.get_by_itag(get_itag)

        print("downloading stream...")
        
        download_stream.download(output_path = r"C:\Users\Jeevan\Desktop\Personal\Personal projects\Youtube Automation AI\Downloaded_playlist_videos")

        counter += 1
        print(f"Download complete {counter}/{(stop_range - start_range)+1} : '{yt.title}'")

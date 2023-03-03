import time,vlc,os

mrl = '/home/terry/Desktop/ent/ngoma/'

vlc_instance =  vlc.Instance()
cele_player = vlc_instance.media_player_new()
playlist = os.listdir(mrl)
for song in playlist:
    if song.endswith('m4a')== False:
        continue 
    spec = mrl+song
    print(spec)
    media = vlc_instance.media_new(spec)
    cele_player.set_media(media)
    cele_player.play()
    time.sleep(1)

    dur = cele_player.get_length()
    print('this song is ',dur/60000,' minutes long')
    time.sleep(dur)

cele_player.stop()
   



#

import vlc
import os
import time
playlist = os.listdir('../../ent/ngoma')

media_player = vlc.MediaPlayer()
for song in playlist:
    print(song)
    my_song = vlc.Media(song)
    media_player.set_media(my_song)

    media_player.play()
    value = media_player.get_time()
    print(value)
    time.sleep(5)

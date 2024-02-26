from win11toast import toast
import spotify_link
import sys

warning = 'icons/alert.ico'

def win11():
    def pause_song():
        spotify_link.sp.pause_playback()

    def skip_song():
        spotify_link.sp.next_track()

    if spotify_link.results is None:
        toast("No Spotify Session Were Found!", "Make sure you have spotify open!", icon=warning)
        sys.exit()
    else:
        name = spotify_link.results['item']['name']
        artist = spotify_link.results['item']['artists'][0]['name']
        cover = spotify_link.results['item']['album']['images'][0]['url']
        url = spotify_link.results['item']['external_urls']['spotify']


        toast(name, artist, icon=cover, on_click=url, audio={'silent': 'true'}, app_id="Notify")
        while 1:
            results = spotify_link.sp.current_user_playing_track()
            if results is not None:
                new_name = results['item']['name']
                new_artist = results['item']['artists'][0]['name']
                new_cover = results['item']['album']['images'][0]['url']
                new_url = results['item']['external_urls']['spotify']
                if new_name != name:
                    toast(new_name, new_artist, icon=new_cover, on_click=new_url, audio={'silent': 'true'}, app_id="Notify")
                else:
                    continue
            else:
                toast("No Spotify Session Were Found!", "Make sure you have spotify open!", icon=warning)
                sys.exit()

from win10toast_click import ToastNotifier
import webbrowser
import spotify_link
import sys

warning = 'icons//alert.ico'


def win10():
    def open_url():
        try:
            webbrowser.open_new(url)
        except:
            print('Failed to open URL. Retry.')

    if spotify_link.results is None:
        toaster = ToastNotifier()
        toaster.show_toast(
            "No Spotify Session Were Found!",
            "Make sure you have spotify open!",
            icon_path=warning,
            duration=5,
        )
        sys.exit()
    else:
        name = spotify_link.results['item']['name']
        artist = spotify_link.results['item']['artists'][0]['name']
        url = spotify_link.results['item']['external_urls']['spotify']

        file_name = 'icons/logo.ico'
        toaster = ToastNotifier()
        toaster.show_toast(
            name,
            artist,
            icon_path=file_name,
            duration=5,
            callback_on_click=open_url
        )
        while 1:
            results = spotify_link.sp.current_user_playing_track()
            if results is not None:
                new_name = results['item']['name']
                new_artist = results['item']['artists'][0]['name']
                url = results['item']['external_urls']['spotify']
                if new_name != name:
                    toaster = ToastNotifier()
                    toaster.show_toast(
                        new_name,
                        new_artist,
                        icon_path=file_name,
                        duration=5,
                        callback_on_click=open_url
                    )
                    name = new_name
                else:
                    continue
            else:
                toaster = ToastNotifier()
                toaster.show_toast(
                    "No Spotify Session Were Found!",
                    "Make sure you have spotify open!",
                    icon_path=warning,
                    duration=5
                )
                sys.exit()


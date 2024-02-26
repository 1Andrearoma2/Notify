import requests
import os
import sys


file_id = "1xNchbQKkmYP8P749wXMcVo_flqoC3nHd"
folder = os.path.join(os.environ['APPDATA'], 'NotifyCache')
if not os.path.exists(folder):
    os.makedirs(folder)
warning = folder + "/alert.ico"

download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

response = requests.get(download_url, stream=True)

if response.status_code == 200:
    with open(warning, "wb") as f:
        for chunk in response.iter_content():
            if chunk:
                f.write(chunk)
else:
    sys.exit()



file_id_logo = "1X3F9wCL6Ql4PDQoqbjSQmzvPp2UltMEl"
folder_logo = os.path.join(os.environ['APPDATA'], 'NotifyCache')
if not os.path.exists(folder_logo):
    os.makedirs(folder_logo)
app_icon = folder_logo + "/logo.ico"

download_url_logo = f"https://drive.google.com/uc?export=download&id={file_id_logo}"

response_logo = requests.get(download_url_logo, stream=True)

if response_logo.status_code == 200:
    with open(app_icon, "wb") as f:
        for chunk in response_logo.iter_content():
            if chunk:
                f.write(chunk)
else:
    sys.exit()
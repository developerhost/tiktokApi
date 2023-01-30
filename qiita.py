from TikTokApi import TikTokApi
import json

# read data from json file, cookie exported from webbrowser
def get_cookies_from_file():
    with open('exported-cookies.json') as f:
        cookies = json.load(f)

    cookies_kv = {} # key-value
    for cookie in cookies:
        cookies_kv[ cookie['name'] ] = cookie['value']
        print ( cookie['name'] + "=" + cookie['value'] )

    return cookies_kv


print('Reading data from cookie file...')
cookies = get_cookies_from_file() #obtiene un dictionary key-value

def get_cookies(**kwargs):
    return cookies

api = TikTokApi()

api._get_cookies = get_cookies 

print("    Requesting data from TikTok")
for video in api.trending.videos():
    print ( video.author.username)
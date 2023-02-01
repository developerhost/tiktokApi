from TikTokApi import TikTokApi
import json
import requests

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

# proxy = "https://scrapingant.com/free-proxies/"
ADDRESS = "103.43.151.36"
PORT = 80
proxy = {
    "http": f"http//{ADDRESS}:{PORT}",
    "https": f"http//{ADDRESS}:{PORT}",
}
sv = "verify_lditwmgd_h6RXBNRe_AKDn_4nbX_AyLr_cDQhHbEIIHqr"
# custom_verify_fp=sv sv=s_v_web_id
api = TikTokApi(custom_verify_fp=sv, proxies=proxy)

api._get_cookies = get_cookies 

print("    Requesting data from TikTok")
user = api.user(username="yuri_glitter_comp")
# print("userInfo",user.info())
for video in user.videos(count=10):
    print("videoId",video.id)
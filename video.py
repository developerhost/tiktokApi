import json

def get_cookies_from_file():
    with open(r'exported-cookies.json') as f:
        cookies = json.load(f)

    cookies_kv = {}
    for cookie in cookies:
        cookies_kv[cookie['ttwid']] = cookie['1%7C3nBozhkwu5OvkbBi44obaTQZJEcv7PMeaYnhyMjXBWc%7C1675075597%7C927f2046ef8de5399be4bad05551f6e156f85218edfca4f39315d16a7124fdf8']

    return cookies_kv


cookies = get_cookies_from_file()


def get_cookies(**kwargs):
    return cookies

from TikTokApi import TikTokApi

api = TikTokApi()

api._get_cookies = get_cookies  

for trending_video in api.trending.videos(count=10):
    print(trending_video)
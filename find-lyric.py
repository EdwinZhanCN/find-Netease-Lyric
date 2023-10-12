#!/usr/bin/env python3

import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)
import requests
import json
import re


def get_lyric(song_id):
    headers = {
        "user-agent": "Mozilla/5.0",
        "Referer": "http://music.163.com",
        "Host": "music.163.com"
    }
    if not isinstance(song_id, str):
        song_id = str(song_id)
    url = f"http://music.163.com/api/song/lyric?id={song_id}&lv=1&tv=-1"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    json_obj = json.loads(r.text)
    return json_obj["lrc"]["lyric"]

def save_lyric_to_lrc(song_id, filename):
    lyric = get_lyric(song_id)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(lyric)


# 使用
while True:
    user_input = input("请输入歌曲链接/link：")
    url = user_input
    match = re.search(r'song\?id=(\d+)', url)
    if match:
        song_id = match.group(1)
        print("Song ID:", song_id)
    else:
        print("No ID found in the URL./没找到歌曲！")
    filename = match.group(1) + ".lrc"
    save_lyric_to_lrc(song_id, filename)



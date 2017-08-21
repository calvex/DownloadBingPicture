# -*- coding: UTF-8 -*-
import requests
import sys
import win32api
import win32con
import win32gui
import os

base_url = 'http://www.bing.com/'

url = base_url + 'HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
r = requests.get(url)
data = r.json()

images = data.get('images', [])

for image in images:
    image_url = image.get('url', '')
    if image_url == '':
        continue
    image_date = requests.get(base_url + image_url)
    file_name = os.path.split(image_url)[1]
    with open(file_name, 'wb') as f:
        f.write(image_date.content)
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, os.path.join(sys.path[0], file_name), 1 + 2)

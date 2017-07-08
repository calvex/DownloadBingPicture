# -*- coding: UTF-8 -*-

import urllib2
import json
import win32gui,win32con,win32api
import sys,os
import datetime
baseurl='http://www.bing.com/'
url=baseurl+'HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
response = urllib2.urlopen(url, timeout=10)
data= json.loads(response.read())
imagesUrl=baseurl+data['images'][0]['url']

imagedata = urllib2.urlopen(imagesUrl, timeout=10)
pos=imagesUrl.rfind("/")+1
filepath = imagesUrl[pos:]
with open(filepath, "wb") as code:
    code.write(imagedata.read())


k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,sys.path[0]+"\\"+filepath, 1+2)

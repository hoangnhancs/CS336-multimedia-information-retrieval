import urllib3  
from bs4 import BeautifulSoup
import re
import requests
import urllib.request
import os

# http = urllib3.PoolManager()

# r = http.request('GET', 'http://travel.com.vn')


# _data = str(r.data)
# f = open('data.txt', 'w')
# _all_data = []
# dem = 0
# print(len(_data.split()))
# _data = _data.split()
# for i in range (len(_data)):
#     if "img" in _data[i] and "src" in _data[i+1]:
#         if 'http' not in _data[i+1]:
#             if '~' in _data[i+1]:
#                 _all_data.append("http://travel.com.vn"+_data[i+1][_data[i+1].find('~')+1:len(_data[i+1])-1])
#             else:
#                 _all_data.append("http://travel.com.vn"+_data[i+1][_data[i+1].find('"')+1:len(_data[i+1])-1])
#         else:
#             _all_data.append(_data[i+1][_data[i+1].find('~')+1:len(_data[i+1])-1])
# #print(_all_data)
# s = ""
# for i in range (len(_all_data)):
#     s += _all_data[i]
#     s += '\n'
#     #print(_all_data[i])
# # print(s)
# f.write(s)







#-*- coding: utf-8 -*-
import io
import random
import shutil
import sys
from multiprocessing.pool import ThreadPool
import pathlib

import requests
from PIL import Image
import time


start = time.time()


def get_download_location():
    try:
        url_input = sys.argv[1]
    except IndexError:
        print('ERROR: Please provide the txt file\n$python image_downloader.py cats.txt')
    name = url_input.split('.')[0]
    pathlib.Path(name).mkdir(parents=True, exist_ok=True)
    return name


def get_urls():
    """
    Returns a list of urls by reading the txt file supplied as argument in terminal
    """
    try:
        url_input = sys.argv[1]
    except IndexError:
        print('ERROR: Please provide the txt file\n Example \n\n$python image_downloader.py dogs.txt \n\n')
        sys.exit()
    with open(url_input, 'r') as f:
        images_url = f.read().splitlines()

    print('{} Images detected'.format(len(images_url)))
    return images_url


def image_downloader(img_url: str):
    """
    Input:
    param: img_url  str (Image url)
    Tries to download the image url and use name provided in headers. Else it randomly picks a name
    """
    print(f'Downloading: {img_url}')
    res = requests.get(img_url, stream=True)
    count = 1
    while res.status_code != 200 and count <= 5:
        res = requests.get(img_url, stream=True)
        print(f'Retry: {count} {img_url}')
        count += 1
    # checking the type for image
    if 'image' not in res.headers.get("content-type", ''):
        print('ERROR: URL doesnot appear to be an image')
        return False
    # Trying to red image name from response headers
    try:
        image_name = str(img_url[(img_url.rfind('/')) + 1:])
        if '?' in image_name:
            image_name = image_name[:image_name.find('?')]
    except:
        image_name = str(random.randint(11111, 99999))+'.jpg'

    i = Image.open(io.BytesIO(res.content))
    download_location = get_download_location()
    i.save(download_location + '/'+image_name)
    return f'Download complete: {img_url}'


def run_downloader(process:int, images_url:list):
    """
    Inputs:
        process: (int) number of process to run
        images_url:(list) list of images url
    """
    print(f'MESSAGE: Running {process} process')
    results = ThreadPool(process).imap_unordered(image_downloader, images_url)
    for r in results:
        print(r)


try:
    num_process = int(sys.argv[2])
except:
    num_process = 10

images_url = get_urls()
run_downloader(num_process, images_url)


end = time.time()
print('Time taken to download {}'.format(len(get_urls())))
print(end - start)
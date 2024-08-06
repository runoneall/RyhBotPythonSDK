import re
import shutil
import sys
import os
import zipfile
import requests

def init_folder(folder_path:str) -> bool:
    print('init download folder ...')
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        os.mkdir(folder_path)
        print('success')
        return True
    except:
        print('failed')
        return False

def is_url(url:str) -> bool:
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def download_file(url:str, save_path:str) -> bool:
    print('download plugin ...')
    try:
        response = requests.get(url, stream=True)
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print('success')
        return True
    except:
        print('failed')
        return False
    
def unzip_file(zip_file_path:str, output_folder:str) -> bool:
    print('start unzip ...')
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
        print('success')
        return True
    except:
        print('failed')
        return False
    
def get_plugin_name(folder_path:str) -> str|None:
    items = os.listdir(folder_path)
    for item in items:
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            return item
    return None

def move_plugin(plugin_path:str, download_plugin_path:str) -> bool:
    if os.path.exists(plugin_path):
        print('Extension already exists! Delete it? (y|n)')
        if input('> ') != 'y':
            return False
        shutil.rmtree(plugin_path)
    shutil.move(download_plugin_path, plugin_path)
    return True

argv = sys.argv
if len(argv) > 1:
    download_url = argv[1]
    download_path = './download/'
    save_path = download_path+'download.zip'
    plugin_path = './Plugins/'

    init_folder(download_path)
    if is_url(download_url):
        if download_file(download_url, save_path):
            if unzip_file(save_path, download_path):
                plugin_name = get_plugin_name(download_path)
                download_plugin_path = download_path+plugin_name
                plugin_path = plugin_path+plugin_name
                if move_plugin(plugin_path, download_plugin_path):
                    print('install finish')
                else:
                    print('install failed')
    
    shutil.rmtree(download_path)

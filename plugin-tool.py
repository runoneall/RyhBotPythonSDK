import importlib
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

    if argv[1] == 'install':
        download_url = argv[2]
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

    if argv[1] == 'loadfile':
        plugin_folder_path = './Plugins/'
        download_folder_path = './download/'
        init_folder(download_folder_path)
        plugin_file_path = argv[2]
        shutil.copy(plugin_file_path, download_folder_path)
        plugin_name = os.path.basename(plugin_file_path)
        save_path = download_folder_path+plugin_name
        if unzip_file(save_path, download_folder_path):
            plugin_folder_name = get_plugin_name(download_folder_path)
            plugin_path = download_folder_path+plugin_folder_name
            if move_plugin(plugin_folder_path+plugin_folder_name, plugin_path):
                print('install finish')
            else:
                print('install failed')
        shutil.rmtree(download_folder_path)

    if argv[1] == 'info':
        plugin_name = argv[2]
        plugin_path = './Plugins/'
        plugin_module = f'./Plugins/{plugin_name}'
        if os.path.exists(plugin_module):
            if plugin_path not in sys.path:
                sys.path.append(plugin_path)
            install = importlib.import_module(f'{plugin_name}.install')
            print(f'Module Name: {install.funcname}')
            print('Attrs:')
            attr_dict = install.attrs
            for attr_name in attr_dict.keys():
                print(f'`- {attr_name} ==> {attr_dict[attr_name]}')
            print(f'Author: {install.author}')
            print(f'Version: {install.version}')
            print('')
            print(install.introduction)
            print('')
            print(f'Module Space: Plugin.{install.funcname}.')
        else:
            print('Module Not Found')

    if argv[1] == 'list':
        plugin_path = './Plugins/'
        plugins = os.listdir(plugin_path)
        i = 1
        for plugin_name in plugins:
            if plugin_name.startswith('plugin_'):
                print(i, plugin_name)
                i += 1

    if argv[1] == 'remove':
        plugin_name = argv[2]
        plugin_path = f'./Plugins/{plugin_name}'
        if os.path.exists(plugin_path):
            shutil.rmtree(plugin_path)
            print('remove success')
        else:
            print('Module Not Found')

else:
    print("Don't Know How To Use?")
    print('''
install   (plugin-tool.py install <url>)          install a plugin from url.
loadfile  (plugin-tool.py loadfile <file path>)   install a plugin from local file.
info      (plugin-tool.py info <plugin name>)     show a plugin info.
list      (plugin-tool.py list)                   list installed plugins.
remove    (plugin-tool.py remove <plugin name>)   delete a plugin.
''')

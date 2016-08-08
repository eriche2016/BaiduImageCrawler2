import os
import re

from  urllib2 import urlopen
from multiprocessing import Pool

####################download function#################################
def download(download_info):
    (url, file_name) = download_info
    for i in range(10): # try 10 times
        try:
            url = urlopen(url, timeout=10)
            data = url.read()
            with open(file_name, 'wb') as out_file:
                out_file.write(data)
                return
        except:
            pass
    print('Download failed: %s'%(url))

####################mass_download function#################################
def mass_download(urls, nthread):
    print('Downloading...')
    #debug_here()
    download_infos = [(url, os.path.basename(url)) for url in urls]

    ##for i in download_infos:
    ##    download(i)

    p = Pool(nthread)
    p.map(download, download_infos)

####################get_html function#################################
def get_html(url_path):
    print('Fetching html...')
    for i in range(5):
        try:
            url = urlopen(url_path, timeout=10)
            s = str(url.read())
            return s
        except:
            pass
    print('Fetching html failed...')


####################get_image_urls function#################################
def get_image_urls(html_content):
    print('Parsing html...')
    exp = 'objURL":"([a-z.:/_A-Z0-9]*)"'
    image_urls = re.findall(exp, html_content)
    print('%d images found in this page'%(len(image_urls)))
    return image_urls

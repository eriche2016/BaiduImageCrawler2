import sys
import os
import argparse

# import utility functions
from libs.utils import *

#from IPython.core.debugger import Tracer
#debug_here = Tracer()


def main(params):
    #key_word = repr(sys.argv[1].encode('UTF-8')).replace('\\x', '%').upper()[2:-1]
    # setting parameters
    key_word = params['key_word']
    dest_folder = params['store_dir']
    num_image = params['num_images']
    nthread = params['num_threads']

    #create and change working directory
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    # changes current directory to des_folder
    os.chdir(dest_folder)

    pn = 0
    cnt = 0
    downloaded = set()
    while cnt < num_image:
        print("Page %d:"%(pn+1))
        image_urls = []

        try:
            url = "http://images.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d&gsm=0"%(key_word, pn*15)
            html_content = get_html(url)
            temp_urls = get_image_urls(html_content)
            for i in temp_urls:
                if i not in downloaded:
                    downloaded.add(i)
                    image_urls.append(i)

            #debug_here()
            mass_download(image_urls, nthread)
        except KeyboardInterrupt:
            exit()
        except:
            pass
        pn += 1
        cnt += len(image_urls)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-key_word',type=str, help="key word to search for images" )
    parser.add_argument('-store_dir',type=str, help="directory used to store the downloaded images" )
    parser.add_argument('-num_images',type=int, help="number of images you wish to download" )
    parser.add_argument('-num_threads', type=int, help="how many threads you wish to download the images", default=1)
    #reading parameters
    if (len(sys.argv) < 5):
        parser.print_help()
        exit(1)

    args = parser.parse_args()
    params = vars(args) # convert to ordinary dict
    main(params)
    print("Done.")

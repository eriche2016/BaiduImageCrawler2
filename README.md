# BaiduImageCrawler2:


This is a multithreaded tool for downloading search results of [Baidu image search](http://images.baidu.com/).

I tailor the repository [BaiduImageCrawler](https://github.com/flexwang/BaiduImageCrawler) to suite my needs to download images from Baidu. 
### Dependencies
  - Python 2.7

### Usage
```sh
$ ./run.sh
```

### Example
you may need to modify `key_words_list` in `run.sh` file
for customized usage.
###Note###
the number of images to be downloaded is at least `-num_images` you specified in [run.sh](https://github.com/eriche2016/BaiduImageCrawler2/blob/master/run.sh#L14), becuause in [crawler.py](https://github.com/eriche2016/BaiduImageCrawler2/blob/master/crawler.py#L29), we will first downloaded before this conditional statements truly works(excluding the staring trival case).

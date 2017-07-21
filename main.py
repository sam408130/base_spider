#-*- coding: utf-8 -*-


"""
-------------------------------------------------
   File Name：     main.py  
   Description :  运行主函数
   Author :       Sam
   date：         2017/7/21
-------------------------------------------------
"""

__author__ = 'Sam'



import logging
import os
import sys
import utils

from scrapy import cmdline

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    if not os.path.exists('log'):
        os.makedirs('log')

    logging.basicConfig(
        filename = 'log/item.log',
        format = '%(levelname)s %(asctime)s: %(message)s',
        level = logging.DEBUG
    )

    utils.log('*******************run spider start...*******************')
    cmdline.execute('scrapy crawl category_urls'.split())
    #cmdline.execute('scrapy crawl item_list'.split())

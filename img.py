# coding=utf-8
# 网络交互
import requests
# 匹配
from bs4 import BeautifulSoup
# 正则
import re
# 系统操作
import os
# 程序睡眠
import time

# 爬虫函数


def SaveImg(_url, _position,_regx):
    '''

    :param url:  网址
    :param _position: 本地位置
    :param _regx: 正则
    :return:
    '''
    url = _url
    position = _position
    #regx = re.compile(_regx)
    # 获取网页代码
    htmll = requests.get(url)
    #html = BeautifulSoup(htmll.text, 'lxml')
    html = htmll.content
    #print html
    print 1
    #pic_url = re.compile(_regx, html)
    pic_url = re.findall(_regx, html, re.S)
    print pic_url
    i = 0
    #print 3
    for link in pic_url:
        #print link
        pic = requests.get(link)
        #print url + link
        # 如果文件夹不存在，则创建一个文件夹
        if 'gif' in link:
            fp = open(position + str(i) + '.gif', 'wb')
            fp.write(pic.content)
        if 'png' in link:
            fp = open(position + str(i) + '.png', 'wb')
            fp.write(pic.content)
        fp = open(position + str(i) + '.jpg', 'wb')
        fp.write(pic.content)
        # print position+each
        fp.close()
        i += 1
        time.sleep(0.5)
        print '正在爬取'








def main():
    #要爬的网页
    url = 'http://www.umei.cc/'
    position_end = ''
    # 本地地址
    position = '/home/python/Desktop/imgs/' + position_end

    _position_end = ''
    # 正则

    regX = '_blank\"><img src="(.*?)" a'

    # 参数 url, 储存位置, 爬取的正则

    SaveImg(url, position, regX)



if __name__ == '__main__':
    main()

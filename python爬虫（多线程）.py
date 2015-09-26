#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-21 17:50:27
# @Author  : jonnyF (fuhuixiang@jonnyf.com)
# @Link    : http://jonnyf.com


import urllib2,re
import os,cookielib
from threading import Thread,Lock
from Queue import Queue
import time

hader={
    'Connection':'Keep-Alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Referer':'http://www.i7wu.cn/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
};
class Fetcher:
    def __init__(self,threads,**hreders):
        self.opener = urllib2.build_opener(urllib2.HTTPHandler)
        self.hreders=hreders
        self.opener.addheaders=[(key,val) for key,val in self.hreders.items()]
        self.lock = Lock() #线程锁
        self.q_req = Queue() #任务队列
        self.q_ans = Queue() #完成队列
        self.threads = threads
        for i in range(threads):
            t = Thread(target=self.threadget)
            t.setDaemon(True)
            t.start()
        self.running = 0
  
    def __del__(self): #解构时需等待两个队列完成
        time.sleep(0.5)
        self.q_req.join()
        self.q_ans.join()
  
    def taskleft(self):
        return self.q_req.qsize()+self.q_ans.qsize()+self.running
  
    def push(self,req):
        self.q_req.put(req)
  
    def pop(self):
        return self.q_ans.get()
  
    def threadget(self):
        while True:
            req = self.q_req.get()
            with self.lock: #要保证该操作的原子性，进入critical area
                self.running += 1
            try:
                ans = self.opener.open(req).read()
            except Exception, what:
                ans = ''
                print what
            self.q_ans.put((req,ans))
            with self.lock:
                self.running -= 1
            self.q_req.task_done()
            time.sleep(0.1) # don't spam
class Browser():
    def __init__(self,startUrl,**hreders):
        self.startUrl=startUrl
        self.hreders=hreders
        self.subDirectory='article'
        self.currentPath=os.getcwd()
        self.suffix='.htm'

    #query first page
    def queryFirstPage(self):
        req=urllib2.Request(self.startUrl)
        [req.add_header(key,val) for key,val in self.hreders.items()]
        html=urllib2.urlopen(req).read()
        reg=re.compile(r'href="(/xiazai/txt/[0-9]{5,}.*?)"')
        url_list=re.findall(reg,html);
        return url_list

    def getSubDirectory(self):
        return os.path.join(self.currentPath,self.subDirectory)

    #create directort and files
    def createDirectory(self,dirName):
        myPath=self.getSubDirectory()
        if not os.path.isdir(myPath):
            os.mkdir(myPath)
        return os.path.join(myPath,dirName)

    def saveFiles(self,content,fileName):
        with open(fileName,'wb') as code:
            code.write(content)

    def buildBrowser(self,*urls):
        cookie=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        opener.addheaders=[(key,val) for key,val in self.hreders.items()]
        links=['http://www.i7wu.cn/mingzhu%s'% x for x in urls]
        return links

if __name__=='__main__':
    browser=Browser('http://www.i7wu.cn/mingzhu/',**hader)
    li=browser.queryFirstPage()
    links=browser.buildBrowser(*li)
    f = Fetcher(threads=len(links),**hader)
    for url in links:
        f.push(url)
    while f.taskleft():
        url,content = f.pop()
        print url,len(content)



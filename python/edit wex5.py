#coding:utf-8 
#Edit appMetadata_in_server.json. http://blog.csdn.net/chenzy945/article/details/18267905
#http://blog.sina.com.cn/s/blog_712ad5c40100qqyv.html
import os, sys,time,string
#import zipfile
import json

print("----------------------------------------------------------------")
print("---------<edit wex5 appMetadata_in_server> by pipihi.com--------")
print("----------------------------------------------------------------")

src = input("Input the path of json file>>")
#fsrc = open(src, "r", encoding="utf-8")
fsrc = open(src, "r", encoding="utf-8")
c = fsrc.read()
print(c)
time.sleep(10)
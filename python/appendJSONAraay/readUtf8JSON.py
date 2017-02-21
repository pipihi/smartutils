#coding:utf-8
#Compression current workspace file.
import os, sys,time
import zipfile,json
import types
print("--------------------------------------")
print("---------<zipcw> by pipihi.com--------")
print("--------------------------------------")
text = open("./demo.json", "r", encoding="utf-8").read();
print("text=" + text)
obj = json.loads(text, encoding="utf-8" )
print("obj=" + json.dumps(obj, ensure_ascii=False))


time.sleep(10)
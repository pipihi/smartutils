#coding:utf-8
#Edit appMetadata_in_server.json.
import os, sys,time,string
#import zipfile
import json

print("----------------------------------------------------------------")
print("---------<edit wex5 appMetadata_in_server> by pipihi.com--------")
print("----------------------------------------------------------------")

src = input("Input the path of json file>>")
#fsrc = open(src, "r", encoding="utf-8")
fsrc = open(src, "r")
print(fsrc)
return
jf = json.load(fsrc);
fsrc.close()

def editVersion(jf) :
	ver = jf["resourceInfo"]["version"]
	print("old version=" + ver)
	ver = ver.split(".")
	i = 0;
	for v in ver :
		ver[i] = int(ver[i])
		i = i + 1
	ver[2] = ver[2] + 1
	ver = str(ver[0]) + "." + str(ver[1]) + "." + str(ver[2])
	print("new version=" + ver)
	jf["resourceInfo"]["version"] = ver
	return jf
jf = editVersion(jf)
dst = open(src, "w", encoding="utf-8")
dst.write(json.dumps(jf,ensure_ascii=False, indent=4))
#print(ver)
print("All done.You can close this window.")
time.sleep(10)
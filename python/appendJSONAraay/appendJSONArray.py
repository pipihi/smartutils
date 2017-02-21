#coding:utf-8
#Compression current workspace file.
import os, sys,time
import zipfile,json
import types
print("--------------------------------------")
#print("---------<zipcw> by pipihi.com--------")
print("--------------------------------------")
src = input("Input the config path>>")
config = json.load(open(src))
demof =  config["demoPath"];
demof = open(demof, "r", encoding="utf-8");
print("Copy data.demoPath=" + config["demoPath"] + "...")
demo = json.load(demof)
demof.close();
idIsString = type(demo[config["idCol"]]) is types.StringType

def _ID(id) :
	if(idIsString) :
		return strID(id)
	else :
		return intID(id)

def strID(id):
	if(type(id) is types.StringType):
		return id
	else:
		return int(id)
def intID(id):
	if(type(id) is types.StringType):
		return int(id)
	else:
		return id
		
fromNum = config["copyFromNum"]
toNum = config["copyToNum"]
fromNum = config["copyFromNum"]
loopNum = config["copyToNum"]

curID = 0;
for element in sample_list:
	print(element[config.idCol])
	


print("All done.You can close this window.")
time.sleep(10)
#coding:utf-8
#Compression current workspace file.
import os, sys,time
import zipfile
print("--------------------------------------")
print("---------<zipcw> by pipihi.com--------")
print("--------------------------------------")

#src = raw_input("Input the path you want to zip>>")
def zipCwFile() :
	src = "./"
	if os.path.isfile(src) :
		print("Error:Not a dir.")
	else :
		dst = "./" + os.path.split(os.getcwd())[1] + ".zip"
		fdst = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
		for root,dirs,files in os.walk(src) :
			#print("root=" + root)
			for file in files :
				full = os.path.join(root,file);
				if full != dst and full != "./zipcw.py" :
					print(full)
					fdst.write(full);
		fdst.close
		return dst
print("Zip file save at " + zipCwFile())

print("All done.You can close this window.")
time.sleep(10)
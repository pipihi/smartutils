#coding:utf-8
#
import os, sys,time
import py2exe
from distutils.core import setup
file = input("Input a .py file you want cover>>")
sys.argv.append('py2exe')
py2exe_options = {
	"includes": ["sip"],
	"dll_excludes":["MSVCP90.dll"],
	"compressed":1,
	"optimize":2,
	"ascii":0,
	"bundle_files": 1,
	}
setup(
	#windows = ["zipcw.py",],
	console = [file],
	#name = '',
	#version = '1.0',
	zipfile = None,
	#options = {'py2exe': py2exe_options}
	)

print("All done.")
time.sleep(10);
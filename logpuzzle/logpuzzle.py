#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib2

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
	"""Returns a list of the puzzle urls from the given log file,
	extracting the hostname from the filename itself.
	Screens out duplicate urls and returns the urls sorted into
	increasing order."""
	def extract_key(url):
		return re.search(r".*-([a-zA-Z]+\.jpg)", url).group(1) 

	def create_url(matchObj):
		path, resource = matchObj.group(1, 2)
		return path + resource

	result = []
	with open(filename) as f:
		logs = f.read().split("\n")
		for log in logs:
			 match = re.search(r"GET (.*/[^/]+/)([\w-]+\.jpg)", log)
			 if match:
				 url = create_url(match)
				 if url not in result:
					 result.append(url)
	result.sort(key=extract_key)
	return result

def download_images(img_urls, dest_dir):
	"""Given the urls already in the correct order, downloads
	each image into the given directory.
	Gives the images local filenames img0, img1, and so on.
	Creates an index.html in the directory
	with an img tag to show each local image file.
	Creates the directory if necessary.
	"""
	count = 0
	if not os.access(dest_dir, "F_OK"):
		os.makedirs(dest_dir)
	os.chdir(dest_dir)
	for url in img_urls:
		image_binary = urllib2.urlopen(url)
		with open("img%02d.jpg" % count, "w") as img:
			img.write(image_binary)
		count += 1
	with open("index.html", "w") as index:
		index.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Puzzle Images</title>\n\t</head>\n\t<body>\n\t\t<h1>Puzzle Images</h1>\n")
		for url in img_urls:
			image = urllib2.urlopen(url)
			with open("img%02d.jpg" % count
			print image
	
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()

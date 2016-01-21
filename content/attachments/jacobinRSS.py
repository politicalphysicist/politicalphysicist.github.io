#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jacobinRSS.py
#
#  Prints an RSS feed for Jacobin Magazine to standard output.
#  
#  Copyright 2013 Chris MacMackin <cmacmackin@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import re
import urllib2
from datetime import datetime

url    = "http://jacobinmag.com/"
title  = "Jacobin Magazine"
dscrpt = "Jacobin is a leading voice of the American left, offering socialist perspectives on politics, economics, and culture. The print magazine is released quarterly and reaches over 5,000 subscribers, in addition to a web audience of 250,000 a month."
header = """<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>
<rss version='2.0' xmlns:content="http://purl.org/rss/1.0/modules/content/">
    <channel>
    <title>{0}</title>
      <link>{1}</link>
      <description>{2}</description>"""
footer = "    </channel>\n</rss>\n"
marker = r'<article id="post-[0-9][0-9][0-9][0-9]"(.*)>'
artcl  = """    <item>
      <title>{0}</title>
      <link>{1}</link>
      <author>{2}</author>
      <pubDate>{3}</pubDate>
      <description>{4}</description>
    </item>"""

print(header.format(title, url, dscrpt))

page = urllib2.urlopen(url + "category/blogs/")
for line in page: 
    item = re.search(marker, line)
    if item:
        for i in range(3):
            page.next()
        headline = page.next()
        
        headline = re.sub(r'(.*)<a href="', '', headline)
        headline =  re.sub(r'</a>(.*)\n', '', headline)
        data = re.split(r'" rel="bookmark">', headline)
        
        for i in range(3):
            page.next()
        summary = page.next()
        summary = re.sub(r'(.*)<p class="entry-synopsis"><p>', '', summary)
        summary = re.sub(r'</p>\n', '', summary)
        
        page.next()
        page.next()
        author = page.next()
        author = re.sub(r'(.*)<p class="entry-author"><a href="(.*)" title="(.*)" rel="author">', '', author)
        author = re.sub(r'</a></p>\n', '', author)
        
        date = page.next()
        date = re.sub(r'(.*)<p class="entry-extra">', '', date)
        date = re.sub(r'</p>\n', '', date)
        dt = datetime.strptime(date, '%m.%d.%y')
        date = dt.strftime('%a, %d %b %Y %I:%M:%S EST')
        
        print re.sub('’', '&#8217;',  artcl.format(data[1],data[0], author,
          date, summary))
page.close()


marker = r'<article id="post-[0-9][0-9][0-9][0-9]" class=" standard post">'
artcl  = """    <item>
      <title>{0}</title>
      <link>{1}</link>
      <author>{2}</author>
      <description>{3}</description>
    </item>"""
issue = ''
page = urllib2.urlopen(url)
for line in page:
    link = re.search(r'<a href="(.*)">In The Magazine</a>', line)
    if link:
        issue = re.sub(r'(.*)<a href="', '', line)
        issue = re.sub(r'">In The Magazine</a>(.*)', '', issue)
page.close()

page = urllib2.urlopen(issue)
for line in page: 
    item = re.search(marker, line)
    if item:
        for i in range(3):
            page.next()
        link = page.next()
        link = re.sub(r'(.*)<a href="', '', link)
        link = re.sub(r'" rel="bookmark">', '', link)
        
        title = page.next()
        title = re.sub(r'( ( )+)', '', title)
        title =  re.sub(r'</a>(.*)\n', '', title)
        
        page.next()
        page.next()
        author = page.next()
        author = re.sub(r'(.*)<p class="entry-author"><a href="(.*)" title="(.*)" rel="author">', '', author)
        author = re.sub(r'</a></p>\n', '', author)
        
        page.next()
        summary = page.next()
        summary = re.sub(r'(.*)<div class="entry-synopsis"><p>', '', summary)
        summary = re.sub(r'</p>\n', '', summary)
        
        print re.sub('’', '&#8217;', artcl.format(title, link, author, summary))
page.close()

print footer

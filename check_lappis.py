#!/usr/bin/env python

import re
import os
import urllib2
from subprocess import Popen, PIPE

post = False
topics = False

with open('latest_link.txt', 'r') as lp:
    last_post = lp.readlines()[0]

ul = "Give your url here"
url_load = urllib2.urlopen(ul)
html_file = url_load.readlines()
url_load.close()

for ln in html_file:
    ln = ln.strip()
    if ln == '<ul id="bbp-forum-2811" class="bbp-topics">':
        topics = True
        continue
    if topics and ln == '<li class="bbp-topic-title">':
        post = True
        continue
    if post and ln.startswith('<a'):
        link = ln.split('"')[3]
        if link != last_post:
            with open('latest_link.txt','w') as np:
                np.write(link)
            p = Popen(['mail', '-s', '"Lappis new post"', 'senthil.biodon@gmail.com'], stdout=PIPE, stdin=PIPE)
            mail_out = p.communicate(input=link)
        post = False
        break

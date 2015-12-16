#!/usr/bin/env python

import re
import os
import urllib2
from subprocess import Popen, PIPE

post = False
topics = False

with open('latest_blocket.txt', 'r') as lp:
    last_post = lp.readlines()[0]

ul = "give your url here"
url_load = urllib2.urlopen(ul)
html_file = url_load.readlines()
url_load.close()

for ln in html_file:
    ln = ln.strip()
    if ln == '<ul class="object-attribute-badges">':
        post = True
        continue
    if post and ln.startswith('<a'):
        link = ln.split('"')[3]
        if link != last_post:
            with open('latest_blocket.txt','w') as np:
                np.write(link)
            p = Popen(['mail', '-s', '"Blocket new post"', 'senthil.biodon@gmail.com'], stdout=PIPE, stdin=PIPE)
            mail_out = p.communicate(input=link)
        post = False
        break

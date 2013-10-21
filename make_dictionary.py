#!/usr/bin/env python
import os
'''\
Download and extract the following url and then run this file from the same 
folder as the extracted files
http://dreamsteep.com/component/docman/doc_download/3-the-english-open-word-list-eowl.html?Itemid=30
'''

os.chdir('EOWL-v1.1.2/LF Delimited Format')
with open('dictionary.txt','w') as f:
    files = os.listdir()
    files.sort()
    for path in files:
        if not 'Words' in path:
            continue
        with open(path) as letter:
            f.write(''.join(letter.readlines()))


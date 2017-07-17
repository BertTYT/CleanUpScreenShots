#! /usr/bin/env python3

import os
import send2trash
import time

os.chdir("/Users/bhidalgo/Desktop")

for file in os.listdir():
    if file.startswith("Screen Shot") and os.stat(file).st_mtime < time.time() - 14 * 86400:
        send2trash.send2trash(file)
        #os.unlink(file)
        #print(file)

#!/usr/bin/env python3
import os
'''
listDir = []
listDir = os.listdir('/home/calst/Downloads')
lenListDir = len(listDir)
if lenListDir > 10:
    os.remove(listDir[1])

print(listDir)
print(len(listDir))
print(lenListDir)
'''

listDir = []
listDir = os.listdir("/home/calst/Downloads")

for X in listDir:
    if len(listDir) > 10:
        listDir = os.listdir("/home/calst/Downloads")
        os.remove(f"/home/calst/Downloads/{listDir[10]}")
        print("ran")
else:
    print("didnt")



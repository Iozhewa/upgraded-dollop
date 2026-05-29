#!/usr/bin/env python3
'''
In case I forget, the file handling trick was horrendously simple
    [1] Upload PDF to Google Drive
    [2] Open PDF with Google Docs
    [3] Download Gdocs PDF as TXT extension
    [4] Copy here for file handling
Assuming everything was transferred neatly...
'''
with open(r"parsers\version2\motec.txt", 'r') as reader:
    lines = reader.readlines()
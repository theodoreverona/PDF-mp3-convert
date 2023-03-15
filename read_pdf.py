# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:04:17 2023

@author: theod
"""


import pyttsx3
import PyPDF2
import os

os.getcwd()
os.chdir("C:\\Users\\theod\\Desktop\\Resume and Cover Letter")

pdfreader = PyPDF2.PdfReader("Theodore Verona CV FS (ENG).pdf")
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', " ")
    print(clean_text)

speaker.save_to_file(clean_text, "Resume_FS.mp3")
speaker.runAndWait()

speaker.stop()

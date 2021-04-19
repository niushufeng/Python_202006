# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:23:52 2021

@author: h3cvdiuser
"""

from sys import argv
from os import listdir
from os.path import join,isfile,isdir
from docx  import Document 
from pptx import Presentation

def checkdocx(dstStr,fn):
    document = Document(fn)
    for p in documnet.paragraphs:
        if dstStr in p.text:
            return True
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                if dstStr in cell.text:
                    return True
                return False
            
            

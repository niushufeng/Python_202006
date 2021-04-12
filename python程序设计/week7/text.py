# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def mergeTxt(txtFiles):
    with open('c:\\result.txt','w') as fp:
        with open(txtFiles[0]) as fp1,open(txtFiles[1]) as fp2:
            while True:
                line1 = fp1.readline()
                if line1:
                    fp.write(line1)
                else:
                    flag = False
                    break
                line2 = fp2.readline()
                if line2:
                    fp.write(line2)
                else:
                    flag = True
                    break
                fp3 = fp1 if flag else fp2
                for line in fp3:
                    fp.write(line)
txtFiles = ['c:\\c1.txt','c:\\c2.txt']
mergeTxt(txtFiles)


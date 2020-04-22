# -*- coding: UTF-8 -*-
from zipfile import ZipFile
import os

#  将全能扫描王的压缩包*.zip解压
#  按月份将所有文件，以月为单位存入Records目录
#  在Records中的月份文件夹中，同步README.md文件内容


zipFilePath = "/练字.zip"

# unzip to 练字 folder
def unzip(filePath):	
    with ZipFile(os.getcwd() + filePath, 'r') as zipObj:
        zipObj.extractall()

def moveFiles():
    sourceFileList = os.listdir(os.getcwd() + "/练字")

    for fileName in sourceFileList:
        print("Move file: " + fileName)

unzip(zipFilePath)
moveFiles()
# -*- coding: UTF-8 -*-
from zipfile import ZipFile
import os
import os.path
from os import path

#  [Done]将全能扫描王的压缩包*.zip解压
#  按月份将所有文件，以月为单位存入Records目录
#  在Records中的月份文件夹中，同步README.md文件内容


zipFilePath = "/练字.zip"
localPath = os.getcwd()

# unzip to 练字 folder
def unzip(filePath):	
    with ZipFile(localPath + filePath, 'r') as zipObj:
        zipObj.extractall()

def moveFiles():
    sourceFileList = os.listdir(localPath + "/练字")

    for fileName in sourceFileList:
        fileInMonth = fileName.split(".")[0].split("_")[1]
        targetFolder = localPath + "/Records/" + fileInMonth
        confirmFolderExist(targetFolder)
        


def confirmFolderExist(filePath):
    if path.isdir(filePath):
        print("Exist folder")
        pass
    else:
        print("Folder not exist,Create it.")
        os.mkdir(filePath) 

unzip(zipFilePath)
moveFiles()
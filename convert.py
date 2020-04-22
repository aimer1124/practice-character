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

        # Check the folder exists
        targetFolder = localPath + "/Records/" + fileInMonth
        confirmFolderExist(targetFolder)

        # move record to Records folder
        os.replace(localPath + "/练字/" + fileName, targetFolder + "/" + fileName)

        # write Record to README
        confirmREADMEExist(targetFolder)

def confirmREADMEExist(filePath):
    fileName = filePath + "/README.md"
    if path.isfile(fileName):
        pass
    else:
        readME = open(fileName,"w")
        readME.close()

def confirmFolderExist(filePath):
    if path.isdir(filePath):
        pass
    else:
        os.mkdir(filePath) 

unzip(zipFilePath)
moveFiles()
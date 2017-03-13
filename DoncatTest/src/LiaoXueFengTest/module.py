'''
Created on 2017-2-10

@author: Lxxx
'''
# _*_ coding: utf-8 _*_
from os import listdir
from os.path import isfile,join
import os.path

def list_all_files(file_path):
    return [f for f in listdir(file_path) if isfile(join(file_path,f))]

def list_all(file_path):
    return listdir(file_path)

def list_all_recruse(file_path,list):
    f=list_all(file_path)
    for file in f:
        if (isfile(join(file_path,file))==False):
            list_all_recruse(join(file_path,file),list)
        else:
            list.append(file)

music=[]
list_all_recruse("D:\\music\\yueyu\\111",music)

groupId="com.hrbb.npas"
artifactId=""
version=""

def generate_coordinate(file_name_list):
    for f in file_name_list:
        lastdot=f.rindex('.')
        filename=f[0:lastdot]
        artifactId=filename[0:filename.rindex('-')]
        version=filename[filename.rindex('-')+1:len(filename)]
#         print(artifactId)
#         print(version)
        print("mvn deploy:deploy-file -DgroupId=com.creditloan.zxcx -DartifactId=%s -Dversion=%s -Dpackaging=jar -Dfile=D:\\music\\yueyu\\111\\%s -Durl=http -DrepositoryId=3rdparty" %(artifactId,version,f))
        print("<dependency>")
        print("<groupId>com.creditloan.zxcx</groupId>")
        print("<artifactId>%s</artifactId>"%(artifactId))
        print("<version>%s</version>"%(version))
        print("</dependency>")

generate_coordinate(music)










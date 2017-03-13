'''
Created on 2017-3-1

@author: Lxxx
'''

from os import listdir
import os.path
from os.path import isfile,join

def was_stop(app_name,was_home,node_name,server_name):
    stopApp=was_home+"/bin/stopApp.jacl"
    
    #获取server name，并存入list：server_list
    server_list=server_name.split('/')
    for server in server_list:
        print("server:%s"%(server))

    #制作stopApp.jacl
    if(os.path.exists(stopApp)):
        os.remove(stopApp);
        
    if(os.path.exists(was_home)):
        print("start to write stopApp.jacl")
        f=open(stopApp,'w')
        for server in server_list:
            f.write("set %s [$AdminControl queryNames node=%s,type=ApplicationManager,process=%s,*]\n"%(server,node_name,server))
            f.write("$AdminControl invoke $%s stopApplication %s\n"%(server,app_name))

was_stop("a","E:\was_deploy_test","node","l/j/r")

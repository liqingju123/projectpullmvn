#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import threading

# 每次都是重启 杀死之前启动的 不然 会端口占用
def kill_9_all_jar():
    os.system("jps |grep NAPSHOT |awk '{print $1}'|xargs kill -9")


def start_server(root_dir, dubbo_registry, project_name):
    path_str = root_dir % (project_name, project_name)
    if (project_name == 'dubbo-registry'):
        path_str = dubbo_registry
    os.system('rm -rf %s/startSh' % path_str)
    os.system(' unzip -o -d   %s/startSh    %s/%s' % (path_str, path_str, '*.zip'))
    os.system(' cp   %s/*.jar  %s/startSh/*/' % (path_str, path_str))
    if (project_name == 'dubbo-registry'):
        return ' java -jar    %s/startSh/*/%s*SNAPSHOT.jar' % (path_str, project_name)
    else:
        return 'java -jar    %s/startSh/*/%s-core*.jar' % (path_str, project_name)

def start_java_project():
    list_dirs = ['dubbo-registry', 'base-center', 'user-center', 'sec-center', 'order-center', 'prod-center']
    root_dir = '/Users/imac/linjiahaoyi_web_new/%s/%s-core/target'
    dubbo_registry = '/Users/imac/linjiahaoyi_web_new/dubbo-registry/target'
    start_str = ''
    for project_name in list_dirs:
        start_str = start_str + '&' + start_server(root_dir, dubbo_registry, project_name)
    os.system(start_str[1:])
          

if __name__ == '__main__':
    kill_9_all_jar()
    start_java_project()
    



    


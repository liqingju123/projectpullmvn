#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import os




def start_java_project():
    list_dirs = ['dubbo-registry', 'base-center', 'user-center', 'sec-center', 'order-center', 'prod-center']
    root_dir = '/Users/imac/linjiahaoyi_web_new/%s/%s-core/target'
    for one_list_dirs in list_dirs:
        for project_name in list_dirs:
            path_str = root_dir % (one_list_dirs, one_list_dirs)
            os.system('rm -rf %s/startSh' % path_str)
            os.system(' unzip -o -d   %s/startSh    %s/%s' % (path_str, path_str, '*.zip'))
            os.system(' cp   %s/*.jar  %s/startSh/*/' % (path_str, path_str))
            os.system(' java -jar    %s/startSh/*/%s-core*.jar' % (path_str, project_name))



if __name__ == '__main__':
    
    start_java_project()
    



    


#!/usr/bin/env python2
#-*- coding: utf-8 -*-

'''
Created on 2017年5月15日
git 更新目录


@author: 李庆举
Already up-to-date

'''
import os
import threading

list_dirs = ['common-parent','dubbo-registry', 'base-center', 'user-center', 'sec-center', 'order-center', 'prod-center','crm-parent','clinic-busi','cache-busi']
root_path ='/Users/imac/linjiahaoyi_web_new/';



def mvn_clean_install_sub(dir_list,one_list_dirs):
    for one_dir_list in dir_list:
            if one_dir_list.endswith('api') or  one_dir_list.endswith('core'):
                os.system('cd     %s/%s/%s  && mvn clean install' % (root_path,one_list_dirs,one_dir_list))
                # 先初始化子项目
       
    os.system('cd     %s/%s  && mvn clean install' % (root_path,one_list_dirs))
    


def git_pull_and_mvn_install(list_dirs):
    for one_list_dirs in list_dirs:
        os.system('cd  %s/%s  && git pull' % (root_path,one_list_dirs))
          
    print '============================================================'
    print '                           git更新完成'
    print '                           git更新完成'
    print '                           git更新完成'
    print '                           git更新完成'
    print '                           git更新完成'
    print '                           git更新完成'
    print '============================================================'

    for one_list_dirs in list_dirs:
        dir_list = os.listdir('%s/%s' %(root_path,one_list_dirs));
        threading.Thread(target=mvn_clean_install_sub,args =(dir_list,one_list_dirs,)).start();



if __name__ =='__main__':
    git_pull_and_mvn_install(list_dirs)

    


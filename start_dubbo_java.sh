#!/bin/bash

root_path="/Users/imac/linjiahaoyi_web_new/${file}/${file}-core/target"

dubbo_registry="/Users/imac/linjiahaoyi_web_new/dubbo-registry/target"

projcet_names=("dubbo-registry" "base-center" "user-center" "sec-center" "order-center" "prod-center" "wechat-center")

jps |grep NAPSHOT |awk '{print $1}'|xargs kill -9
unzip -o -d  "${dubbo_registry}/startSh"    "${dubbo_registry}/*.zip"
cp  ${dubbo_registry}/*.jar		${dubbo_registry}/startSh/*/


start_jar_sh="java  -jar ${dubbo_registry}/startSh/*/${projcet_names[0]}*SNAPSHOT.jar  > /dev/null"

for file in ${projcet_names[@]:1};
	do
	root_path="/Users/imac/linjiahaoyi_web_new/${file}/${file}-core/target"
	unzip -o -d  "${root_path}/startSh"    "${root_path}/*.zip"
	cp  	${root_path}/*.jar		${root_path}/startSh/*/
	start_jar_sh="${start_jar_sh}  &  java -jar    ${root_path}/startSh/*/${file}-core*.jar  "
	
done


eval $start_jar_sh  #  使用 eval $函数进行二次扫描 解决直接执行找不到class类的情况

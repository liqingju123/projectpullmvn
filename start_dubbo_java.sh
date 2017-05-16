#!/bin/bash

root_path="/Users/imac/linjiahaoyi_web_new/${file}/${file}-core/target"

dubbo_registry="/Users/imac/linjiahaoyi_web_new/dubbo-registry/target"

projcet_names=("dubbo-registry" "base-center" "user-center" "sec-center" "order-center" "prod-center")

jps |grep NAPSHOT |awk '{print $1}'|xargs kill -9


unzip -o -d  "${dubbo_registry}/startSh"    "${dubbo_registry}/*.zip"
cp  ${dubbo_registry}/*.jar		${dubbo_registry}/startSh/*/


start_jar_sh="java  -jar ${dubbo_registry}/startSh/*/${projcet_names[0]}*SNAPSHOT.jar "

for file in ${projcet_names[@]:1};
	do
	root_path="/Users/imac/linjiahaoyi_web_new/${file}/${file}-core/target"
	unzip -o -d  "${root_path}/startSh"    "${root_path}/*.zip"
	cp  	${root_path}/*.jar		${root_path}/startSh/*/
	start_jar_sh="${start_jar_sh}  &  java -jar    ${root_path}/startSh/*/${file}-core*.jar  "
	
done

# sleep 10
echo $start_jar_sh > start_jar_sh.sh

sh start_jar_sh.sh
# $start_jar_sh

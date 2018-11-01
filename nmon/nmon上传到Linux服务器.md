## 一、简介
nmon是一个简单的性能监测工具监控linux和unix，可以监测CPU、内存、网络等的使用情况。它是一个系统监视、调优、性能测试工具，它能一次性提供大量性能相关的信息。
## 二、安装
   ###### 下载地址
nmon:http://nmon.sourceforge.net/pmwiki.php?n=Site.Download

nmon analyzer:
https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Power+Systems/page/nmon_analyser

nmonchart:
http://nmon.sourceforge.net/pmwiki.php?n=Site.Nmonchart
## 三、详细步骤
    我的环境 :centos7
  1.下载nmon 并放到linux中/opt目录
 
  2.建个nmon目录：mkdir nmon
  
  3.nmon主题程序（nmon16g_x86.tar.gz），解压并给权限tar xvf nmon16g_x86.tar.gz
  
  4.改成nmon mv nmon16g_x86_rhel72 nmon 
  
  5.给权限755 chmod 755nmon
  
  6.运行 ./nmon（在nmon目录下执行命令）
  
 ## 四、实时监控

输入以下命令：

c   可显示CPU的信息

m   对应内存

n   对应网络

d   可以查看磁盘信息

t   可以查看系统的进程信息
 
 ## 五、采集监控数据
1. 连接命令：ln -s /opt/nmon/nmon /usr/bin/

2.上传nmonchart34.tar到nmon目录下，并解压 tar xvf nmonchart34.tar
  
3.使用nmonchart把.nmon转换成.html
    ,nmonchart是ksh,我的系统中没有ksh
    所以安装 yum install ksh
  
4.生成数据参数nmon -s1 -c300 -f -m /opt/nmon

-    -s 每隔多少秒刷新一次屏幕，就是每隔多少秒记录一次数据
-    -c 刷新次数，就是记录次数
-    -f 电子表格输出格式，形成一个可以以Excel表解读的数据集。
-    -m 生成的文件输出到哪个目录
## 六、生成图形化报表
 1    ./nmonchart localhost_181016_1049.nmon test1.html（./nmonchart 接文件名，再接生成html）
  2. html查看需要翻墙查看<script type="text/javascript" src="https://www.google.com/jsapi"></script>
  3. 不翻墙需要修改：<script type="text/javascript" src="jsapi.js"></script>
## 七、结果分析

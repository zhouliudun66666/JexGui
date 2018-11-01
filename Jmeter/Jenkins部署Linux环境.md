1、vm获取ip

2、把Java丢入/usr目录

3、查看并删除自带openJDK  rpm -aq|grep jdk|xargs rpm -e --nodeps

4、chmod 755 -R java/ 把Java文件给予权限

5、cd /etc  删除配置文件rm -rf profile 

6、替换profile文件 配置生效source /etc/profile

7、usr/local 放文件（ant\jmeter\）

8、Jenkins.war 放到 /usr/java/apache-tomcat-9.0.4/webapps/路径

9、启动Jenkins /usr/java/apache-tomcat-9.0.4/bin/ 启动./startup.sh
关闭.shutdown.sh

10.获取密码 cat/root/.jenkins/crots/init....
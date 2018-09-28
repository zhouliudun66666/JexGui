### Jmeter+Ant+Jenkins接口自动化测试框架搭建

#### 1.安装Jmeter

(1)下载安装包

参考资料

(2)配置环境变量

参考资料

(3)安装验证

命令窗口输入jmeter -v ，出现版本信息则安装成功

#### 2.安装Ant

(1)安装包下载

下载路径：http://ant.apache.org/bindownload.cgi(可参考)

(2)配置环境变量

参考资料

(3)安装验证

命令行输入ant -v ，出现版本信息则安装成功

3.安装Jenkins

在Jenkins.war文件当前目录下，执行命令：java -jar Jenkins.war(通过war包安装，也可参考其他安装方式)

#### 3.Ant配置Jmeter

原理:用ant命令来调动执行jmeter接口测试，并生成测试报告

(1)将jmeter extras目录下的ant-jmeter-1.1.1.jar文件拷贝到ant安装目录下的lib文件夹中(ant运行时才能找到"org.programmerplanet.ant.taskdefs.jmeter.JMeterTask"这个类，之后可以触发Jmeter脚本)

(2)配置ant的编译文件 build.xml, 需要按实际情况修改文件(已附上)

(3)在找到jmeter.properties文件，在jmeter/bin目录下，打开该文档并编辑，修改jmeter报告输出格式为xml：改jmeter.save.saveservice.output_format=csv为jmeter.save.saveservice.output_format=xml，并且去掉前面的注释符号#

验证配置，执行构建测试：

将jmeter的一个脚本保存，并将build.xml配置文件放在与测试脚本相同的目录下，
在当前目录下，执行ANT命令，提示BUILD SUCCESSFUL，则说明构建测试成功

#### 4.Jenkins持续集成

(1)安装插件

安装Performance plugin、HTML Publisher plugin、Ant Plugin 等插件

功能：用例生成测试报告

(2)添加ANT、JDK、GIT

系统管理-全局工具配置

JDK ：

别名：JDK  

JAVA_HOME:C:\Program Files\Java\jdk1.8.0_181(本地路径)

Ant :

NAME：apache-ant-1.10.5

ANT_HOME：C:\Users\jex\Desktop\apache-ant-1.10.5(本地路径)

(3)配置邮箱

在Extended E-mail Notification项，配置邮箱相关内容，具体可参考链接https://www.jianshu.com/p/8b33585ccc1c

(4)后续优化，再继续补充



 













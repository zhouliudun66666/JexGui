### 一、Linux——centos docker安装
#yum install -y docker
#启动docker #service docker start
#docker --version验证是否OK
### 二、Pinpoint
1.克隆文档opt目录下 git clone https://github.com/naver/pinpoint-docker.git
或者下载pinpoint-docker-master.zip 解压之后改名mv pinpoint-docker-master/ pinpoint-docker


2.pip 安装docker-compose：

$ yum -y install epel-release


$ yum -y install python-pip


$ pip install docker-compose

可能需要修改要修改要修改docker-compose.yml 里面
 里面
 里面


volumes:


./home/pinpoint/hbase


./home/pinpoint/zookeeper


的路径为绝对路径如：/opt/pinpoint/hbase，/opt/pinpoint/zookeeper

输入命令
docker-compose pull && docker-compose up -d
### 三、docker安装web可视化管理工具之一 portainer：
#docker volume create portainer_data

 #docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer

浏览器页面：http://192.168.244.129:9000/#/containers

http://192.168.244.129:8079/#/main/
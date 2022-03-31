# DOCKER

## 教程

### 中文文档

https://docker.easydoc.net/doc/81170005/cCewZWoN/lTKfePfP

### 官方文档

https://docs.docker.com/get-started/

## 加装hyper v

https://blog.csdn.net/null111666/article/details/103958158

```
pushd "%~dp0"

dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt

for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"

del hyper-v.txt

Dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /LimitAccess /ALL
```

## Ubuntu镜像

https://hub.docker.com/_/ubuntu?tab=tags

anaconda镜像

https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/



## docker run

https://blog.csdn.net/m0_38027358/article/details/87376517

docker run -it -p 180:180 haoquan1999/ai_composer  /bin/bash

docker run -it -p 180:180 heroku/heroku:18 /bin/bash

docker run -it -p 180:180 ubuntu:16.04 /bin/bash

docker run -it -p 180:180 haoquan1999/ai_composer  /bin/bash

docker run -it -p 80:80 tensorflow/tensorflow:0.8.0 /bin/bash

**-i:** 以交互模式运行容器，通常与 -t 同时使用；

**-t:** 为容器重新分配一个伪输入终端，通常与 -i 同时使用；

**-p:** 指定端口映射，格式为：主机(宿主)端口:容器端口 



## docker start

https://zhidao.baidu.com/question/245146971591809124.html

docker start -ia <containerid>



## docker位置

wsl默认保存在C:\Users<主机名>\AppData\Local下



## TensorFlow

https://hub.docker.com/r/tensorflow/tensorflow/tags?page=1&ordering=-last_updated

docker pull tensorflow/tensorflow:0.8.0

https://www.tensorflow.org/install/docker





## 保存镜像

```
docker commit -m="has update" -a="hq" e218edb10161 memo:v2
```

各个参数说明：

- **-m:** 提交的描述信息
- **-a:** 指定镜像作者
- **e218edb10161：**容器 ID
- **runoob/ubuntu:v2:** 指定要创建的目标镜像名

我们可以使用 **docker images** 命令来查看我们的新镜像 **runoob/ubuntu:v2**：



https://www.runoob.com/docker/docker-image-usage.html

## 上传镜像

https://www.cnblogs.com/lgjlife/p/10982565.html

```
docker push haoquan1999S/ubuntu:vim  
```

必须是dockerhub的用户名/项目名称:版本

## Docker镜像源

```
{
  "builder": {
    "gc": {
      "defaultKeepStorage": "20GB",
      "enabled": true
    }
  },
  "experimental": false,
  "features": {
    "buildkit": true
  },
  "registry-mirrors": [
    "https://2g028uyf.mirror.aliyuncs.com"
  ]
}
```

## Docker自启动

### 执行多条shell

sh -c "ls && echo '-------' &&  ls"

https://blog.csdn.net/weixin_30642267/article/details/98671653

### 自启动

https://blog.csdn.net/qq_37312838/article/details/115710209

https://blog.csdn.net/qq_34173549/article/details/79824541

### 自启动命令+端口转发+挂载文件夹

docker run -p 5001:5000 -p 1999:1999 --restart=always -v /autorun:/home/autorun  -it ai_composer:v2 

### 自启动命令+端口转发+自动运行

docker run -p 5001:5000 -p 1999:1999 --restart=always  -it interface sh -c "cd home/AI_Composer && python generateMusicInterFace.py"

### 自启动命令+端口转发+自动运行+后台运行（-d）

docker run -p 5001:5000 -p 1999:1999 --restart=always  -d interface sh -c "cd home/AI_Composer && python generateMusicInterFace.py"


# Git

## git init

初始化本地仓库



## 基本配置

git config --global user.name "hq"

git config --global user.email "744204541@qq.com"

ssh-keygen -t [rsa](https://so.csdn.net/so/search?q=rsa&spm=1001.2101.3001.7020) -C "744204541@qq.com"



然后打开C:\Users\HQ \ .ssh 里面的id_rsa.pub，复制到

https://github.com/settings/keys

（登录github，然点头像，setting，然后左边SSH and GPG keys）



## 远程仓库设置

添加远程版本库：

```
git remote add [shortname] [url]
```

shortname 为本地的版本库，例如：

```
# 提交到 Github
$ git remote add origin git@github.com:tianqixin/runoob-git-test.git
$ git push -u origin master
```

其他

```
git remote rm name  # 删除远程仓库
git remote rename old_name new_name  # 修改仓库名
```

在github上创建仓库，复制仓库的ssh地址

git remote add origin git@github.com:CHINA-N01/Document.git





## git add





## git commit -m ‘本次提交的说明'





## git push

git push origin与git push -u origin master的区别

上面命令表示，将当前分支推送到origin主机的对应分支。 

如果当前分支只有一个追踪分支，那么[主机名](https://so.csdn.net/so/search?q=主机名&spm=1001.2101.3001.7020)都可以省略。 

$ git push 如果当前分支与多个主机存在追踪关系，那么这个时候-u选项会指定一个默认主机，这样后面就可以不加任何参数使用git push。

$ git push -u origin master 上面命令将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push了。

 不带任何参数的git push，默认只推送当前分支，这叫做simple方式。此外，还有一种matching方式，会推送所有有对应的远程分支的本地分支。Git 2.0版本之前，默认采用matching方法，现在改为默认采用simple方式。



https://blog.csdn.net/qq_15899635/article/details/88421585



第一次push用

git push -u origin master



## 其他

https://blog.csdn.net/liuweixiao520/article/details/78971221
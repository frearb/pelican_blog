---
title: 利用ssh跳板功能登陆虚拟机集群
category:
date: 2019-03-12 15:14:57
tags: linux
---
![图示](/images/computer.jpg)
使用ssh命令提供的跳板功能，假设存在3台服务器S1、S2、S3，S1与S2可以互通，S2与S3可以互通，由于网络隔离S1与S3不能互通，此时可以在S1上将S2作为跳板登陆S3,命令为：
```bash
ssh -J S2 S3
```
假设在S1上登陆S2、S3需要指定特定的用户名端口私钥，在上述命令中S2的私钥无法指定，可以通过修改config文件来指定或者使用`-J`参数的展开形式：
```bash
ssh  -o ProxyCommand="ssh -i id_rsa2 -W %h:%p -p 22 jump@S2" S3 -p 22 -i id_rsa3 
```
  假设S3不是一台服务器而是一个虚拟机集群，内部包含了虚拟机S31、S32、S33、S34、S35等若干台虚拟机，S2作为专用跳板供外部机器连接虚拟机。在S2上新建专用用户`jump`，设置该用户通过密钥登录并且将默认shell改为`nologin`以阻止常规登录，只允许作为跳板。

  将上述命令封装为一脚本文件`sshb`，内容如下：
```bash
#!/bin/bash
(cat <<EOF
-----BEGIN RSA PRIVATE KEY-----
**跳板机上用户jump的私钥，该私钥公开使用**
-----END RSA PRIVATE KEY-----
EOF
) > /tmp/jump_rsa
chmod 600 /tmp/jump_rsa
ssh -o "StrictHostKeyChecking no" -o ProxyCommand="ssh -o 'StrictHostKeyChecking no' -i /tmp/jump_rsa -W %h:%p -p 22 jump@10.0.4.105" $*
rm /tmp/jump_rsa
```
  之后即可通过 `./sshb S31`来登录虚拟机。
  `S31`为某台虚拟机的别称，该别称可以记录在本机的`.ssh/config`文件或`/etc/hosts`文件或者跳板机S2的`/etc/hosts`文件中。
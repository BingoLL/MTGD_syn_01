### www.mutougeda.cn
for the web site.2018-02-06

>### 本站源码使用（默认Linux系统）：

>1. python3环境：
>>如果没有安装virtualenv，请 pip3 install virtualenv，然后virtualenv  env_name(Python 虚拟环境名字任意,目录任意)即可创建Python3环境，然后启用该Python环境：source env_name/bin/activate

>2. 下载源码：
>>git clone git@github.com:BingoLL/MTGD_syn_01.git

>3. 安装Python包：
>>cd MTGD_syn_01 进入当前源码目录 ，注意保持在上一步启用的Python3环境中，或者你自建的其他Python3环境，执行 pip install -r plist.txt ，即可安装完成本程序所依赖的Python包。

>4. 修改settings:
>>将DEBUG值改为True，根据你的习惯修改settings中static和media根目录位置，也可以在系统中创建settings中的目录，并赋予 777 权限 ：sudo chmod 777 /var/www/web_MTGD

>5. 迁移数据库，搜集静态文件，进入浏览器 127.0.0.1:8000查看网站效果。

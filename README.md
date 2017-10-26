# xbman-blog
一个简单的个人博客，优雅的页面，简单的后台。如丝般顺滑~
 
点击 [博客](https://www.xbman.cn/ "博客") 查看演示效果

更新记录：

    2017年10月26日
        首页增加了原创/转载标识，可在后台设置哦
        首页增加了作者显示小标识，方便多人维护时展示作者名字
        后台登陆增加了验证码功能
        修复了各种bug。

### 截图：

首页

![首页](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/index.jpg "首页")

关于

![关于](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/about.jpg "关于")

后台登陆

![后台登陆](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/houtai.jpg "后台登陆")

后台

![后台](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/admin.jpg "后台")

添加博文

![添加博文](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/tianjia.jpg "添加博文")


### 部署方法：

    1、部署环境
        python2.7.10+django1.8.3
    2、开始部署(nginx+gunicorn方式)
   
        - 首先安装python2.7+pip （具体安装方式自行百度。）
        - 安装基本环境 pip install -r requrements.txt #重要步骤。
        - gunicorn  -w 2 xbmanblog.wsgi:application -b 0.0.0.0:8080 -D --log-level=INFO --timeout=100
        - nginx和gunicorn结合（自行百度）
        - 创建后台账号请使用:python manage.py create createsuperuser


#xbman-blog
一个简单的个人博客，优雅的页面，简单的后台。如丝般顺滑~

###截图：

首页

![首页](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/index.jpg "首页")

关于

![关于](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/about.jpg "关于")

后台

![后台](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/admin.jpg "后台")

添加博文

![添加博文](https://git.oschina.net/weihaoxuan/images/raw/master/xbman-blog/tianjia.jpg "添加博文")


部署方法：
    1、部署环境
        python2.7.10+django1.8.3
    2、开始部署
        nginx+gunicorn
        首先安装python2.7+pip （具体安装方式自行百度。）
        安装基本环境 pip install -r requrements.txt
        gunicorn  -w 2 xbmanblog.wsgi:application -b 0.0.0.0:8080  --log-level=INFO --timeout=100
        nginx和gunicorn结合（自行百度）



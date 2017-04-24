#xbman-blog
一个简单的个人博客，优雅的页面，简单的后台。如丝般顺滑~

部署方法：
    1、部署环境
        python2.7.10+django1.8.3
    2、开始部署
        nginx+gunicorn
        首先安装python2.7+pip （具体安装方式自行百度。）
        安装基本环境 pip install -r requrements.txt
        gunicorn  -w 2 xbmanblog.wsgi:application -b 0.0.0.0:8080  --log-level=INFO --timeout=100
        nginx和gunicorn结合（自行百度）



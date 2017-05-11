# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
from django.contrib import auth
from django.template.context import RequestContext
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk.basic import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
import models
import utils
# Create your views here.
from django.utils.safestring import mark_for_escaping

WECHAT_TOKEN = 'weixinwakaka'
# APP_ID = 你的app id
# APP_SECRET = 你的app secret


# 实例化 WechatBasic
wechat_instance = WechatBasic(token=WECHAT_TOKEN)


def index(request):
    articles = models.Article.objects.filter(status=0).order_by('-created_time')
    page = request.GET.get('page', 1)
    tag = request.GET.get('tag')
    categories = request.GET.get('category')
    seriess = request.GET.get('series')
    if tag:
        T = models.Tag.objects.get(name=tag)
        articles = articles.filter(tag=T)
    if categories:
        C = models.Categories.objects.get(name=categories)
        articles = articles.filter(categories=C)
    if seriess:
        S = models.Series.objects.get(name=seriess)
        articles = articles.filter(series=S)
    paginator = Paginator(articles, 10, request=request)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    tags = models.Tag.objects.all()
    links = models.Link.objects.all()
    categories = models.Categories.objects.all()
    series = models.Series.objects.all()
    return render(request, 'index.html',{'articles': articles,'links': links,'tags': tags,
                                         'categories': categories,'series':series,
                                         'theme':utils.setsession(request)},
                  context_instance=RequestContext(request))

def as_view(request,article_url):
    article = models.Article.objects.get(id=article_url)
    article.read += 1
    article.save()
    url = 'http://' + request.get_host() + request.get_full_path()
    series = models.Series.objects.all()
    return render(request, 'article.html',{'article': article,"url":url,'series':series,'theme':utils.setsession(request)},
                  context_instance=RequestContext(request))


def about(request):
    try:
        article_body = models.Setting.objects.get().body
    except Exception:
        article_body = u'####博主很懒什么都没留下:tw-1f33f:！'
    series = models.Series.objects.all()
    return render(request, 'about.html', {'body': article_body,'series':series,'theme':utils.setsession(request)},
                  context_instance=RequestContext(request))


@csrf_exempt
def weixin(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')

        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")

    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')

    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()

    # 关注事件的默认回复
    response = wechat_instance.response_text(
        content=(
            '哎呀妈呀，老铁你来啦！/:<L>欢迎来到可能是全行业最专业，最权威，博主长的最帅/:B-)，才华横溢的魏先森个人订阅号，在这里我会分享各种技术帖子，咱们一起成长！/:share\n回复【来吧骚年】查看本订阅号支持的全部功能'
            '\n【<a href="http://www.xbman.cn">魏先森的博客</a>】'
        ))

    if isinstance(message, TextMessage):
        # 当前会话内容
        content = message.content.strip()
        if content == '来吧骚年':
            reply_text = (
                '哈哈，铁子你可以使用如下指令来获取相关信息：\n1. 输入【博客】来查看我的博客\n'
                '2. 关键字查找教程集，例如【python教程】【django教程】\n'
                '还有更多功能正在开发中哦 ^_^\n'
                '【<a href="http://www.xbman.cn"">我的博客</a>】'
            )
        elif content == '博客':
            reply_text = '我的博客地址是 http://www.xbman.cn"'
        elif '教程' in content:
            key = content.strip('教程')
            # reply_text = models.KeyWord.objects.get(keyword=key).content
            try:
                keyword_object = models.KeyWord.objects.get(keyword=key)
                reply_text = keyword_object.content
                reply_text = json.loads(reply_text)
            except models.KeyWord.DoesNotExist:
                try:
                    reply_text = models.KeyWord.objects.get(keyword='提示').content
                    reply_text = json.loads(reply_text)
                except models.KeyWord.DoesNotExist:
                    reply_text = ('/:P-(好委屈，数据库翻个遍也没找到你输的关键词！\n'
                                  '试试下面这些关键词吧：\npython教程,django教程\n'
                                  '感谢您的支持！/:rose'
                                  )
        else:
            reply_text = '/:@)功能还在开发中哦,欢迎老铁提出宝贵意见哦/:heart！访问到【<a href="http://www.xbman.cn"">我的博客</a>】，联系我哦！'
        response = wechat_instance.response_text(content=reply_text)
    return HttpResponse(response, content_type="application/xml")

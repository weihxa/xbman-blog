#!/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import models
import json
from wechat_sdk.basic import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
from django.http import HttpResponse ,HttpResponseBadRequest

WECHAT_TOKEN = 'weixinwakaka'


# 实例化 WechatBasic
wechat_instance = WechatBasic(token=WECHAT_TOKEN)

def Obtain(request):
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

def Obtain_post(request):
    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')

    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()

    # 关注事件的默认回复
    try:
        reply_text = models.wxsetting.objects.get(keyword='关注').content
        reply_text = json.loads(reply_text)
    except Exception:
        reply_text = (
            '哎呀妈呀，老铁你来啦！/:<L>欢迎来到可能是全行业最专业，最权威，博主长的最帅/:B-)，才华横溢的魏先森个人订阅号，在这里我会分享各种技术帖子，咱们一起成长！/:share\n回复【来吧骚年】查看本订阅号支持的全部功能'
            '\n【<a href="http://www.xbman.cn">魏先森的博客</a>】'
        )
    response = wechat_instance.response_text(
        content=reply_text)
    if isinstance(message, TextMessage):
        # 当前会话内容
        content = message.content.strip()
        if '教程' in content:
            key = content.strip('教程')
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
            try:
                reply_text = models.wxsetting.objects.get(keyword=content).content
                reply_text = json.loads(reply_text)
            except Exception:
                try:
                    reply_text = models.wxreply.objects.order_by('?')[:1]
                    reply_text = json.loads(reply_text[0].content)
                except Exception:
                    reply_text = ('/:@)功能还在开发中哦,欢迎老铁提出宝贵意见哦/:heart！访问【<a href="http://www.xbman.cn"">我的博客</a>】，联系我哦！')
        response = wechat_instance.response_text(content=reply_text)
    return HttpResponse(response, content_type="application/xml")
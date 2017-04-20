#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'weihaoxuan'

import random

def rnumber():
    return random.randint(1,4)


def setsession(request):
    try:
        theme = request.session["theme"]
    except Exception, e:
        theme = rnumber()
        request.session['theme'] = theme
        request.session.set_expiry(60)
    return theme
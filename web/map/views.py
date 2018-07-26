# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import testdata

# 主页   localhost:8110
# 主页    localhost:8110/index/
def index(request):
    return render(request, 'map/index.html')


# 热力图
def heat(request):
    return render(request, 'map/heat.html')


# 散点图
def scatter(request):
    return render(request, 'map/scatter.html')


# 柱状图
def histogram(request):
    return render(request, 'map/histogram.html')

def form(request):
    return render(request,'map/form.html')
# post接收地址
def data(request):
	if request.method=='POST':
		text=request.POST.get('text')
		print text
		testdata.main(text)
    # 跳转到热力图
    	return redirect('/heat/')

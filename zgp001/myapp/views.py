from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
import re


from .models import Rotation,Menu,Commodity_kind,Commodity,Jdmsb,Fxhhb,Ppmsb,Hmzjb
def main(request):
    #轮播图
    rotlist = Rotation.objects.all()
    #特殊商品展示
    meaulist = Menu.objects.all()
    #大菜单
    commodityKindlist= Commodity_kind.objects.all()[:5]
    #商品展示
    commoditylist= Commodity.objects.all()
    #京东秒杀
    jdmslist=Jdmsb.objects.all()
    #发现好货
    fxhhlist=Fxhhb.objects.all()
    #品牌秒杀
    ppmslist=Ppmsb.objects.all()
    #会买专场
    hmzjlist=Hmzjb.objects.all()

    return render(request,'myapp/main.html',{'title':'主页','rotlist':rotlist,'meaulist':meaulist,'commodityKindlist':commodityKindlist,'commoditylist':commoditylist,'jdmslist':jdmslist,'fxhhlist':fxhhlist,'ppmslist':ppmslist,'hmzjlist':hmzjlist})

def ken(request):
    commoditylist = Commodity.objects.filter(co_kind=4)
    return render(request,'myapp/ken.html',{'title':'闪购','commoditylist':commoditylist})
def kenview(request):
    comp=request.GET.get('aa')
    compids = Commodity_kind.objects.values()
    for i in compids:
        if i['ct_name'] == comp:
            compID=i['ct_id']
    list=[]
    commoditylist = Commodity.objects.filter(co_kind=compID)
    for commodity in commoditylist:
        list.append([commodity.co_image,commodity.co_pice,commodity.co_brief_introduction,commodity.co_id])
    return JsonResponse({'data':list})
def car(request):
    return render(request,'myapp/car.html',{'title':'购物车'})
def mean(request):
    return render(request,'myapp/mean.html',{'title':'我的'})
def register(request):
    return render(request, 'myapp/register.html')
def sign(request):
    return render(request, 'myapp/sign.html')




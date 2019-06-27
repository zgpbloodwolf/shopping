from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
import re
from .models import Rotation,Menu,Commodity_kind,Commodity,Jdmsb,Fxhhb,Ppmsb,Hmzjb,Usercar
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
    commoditylist = Commodity.objects.filter(co_kind=4).values()
    carnumberlist={}
    if  Usercar.objects.all():
        usercarlist = Usercar.objects.values()
        for usercar in usercarlist:
            coid = usercar["car_co"]
            num = usercar["car_number"]
            carnumberlist[coid]=num
        print('\n\n')
        return render(request, 'myapp/ken.html', {'title': '闪购', 'commoditylist': commoditylist, 'number': carnumberlist})
    else:
        return render(request,'myapp/ken.html',{'title':'闪购','commoditylist':commoditylist,'number':0})

def kenview(request):
    comp = request.GET.get('aa')
    compids = Commodity_kind.objects.values()
    for i in compids:
        if i['ct_name'] == comp:
            compID=i['ct_id']
    list=[]
    commoditylist = Commodity.objects.filter(co_kind=compID)
    for commodity in commoditylist:
        if Usercar.objects.filter(car_co=commodity.co_id).exists():
            number = Usercar.objects.filter(car_co=commodity.co_id).values()[0]['car_number']
            list.append([commodity.co_image, commodity.co_pice, commodity.co_brief_introduction, commodity.co_id, number])
        else:
            list.append([commodity.co_image,commodity.co_pice,commodity.co_brief_introduction,commodity.co_id,0])
    return JsonResponse({'data':list})
def addchange(request):
    car_id = int(request.GET.get('car_id'))
    co = Commodity.objects.get(co_id=car_id)
    if not Usercar.objects.filter(car_co=car_id).exists():
        usercar = Usercar()
        #用户
        usercar.car_user = '111'
        #商品id
        usercar.car_co = car_id
        #数量
        usercar.car_number = 1
        #选中状态
        usercar.car_sele = 1
        #价格
        usercar.car_money = Commodity.objects.filter(co_id=car_id).values()[0]["co_pice"]
        usercar.save()
        co.co_number = co.co_number - 1
        co.save()
        return JsonResponse({"data":1})
    else:
        maxnumber = Commodity.objects.filter(co_id=car_id).values()[0]["co_number"]
        number = Usercar.objects.filter(car_co=car_id).values()[0]["car_number"]
        if maxnumber > 0:
            number += 1
            us = Usercar.objects.get(car_co=car_id)
            co.co_number = co.co_number - 1
            co.save()
            us.car_number = number
            us.save()
            return JsonResponse({'data': number})
        else:
            return JsonResponse({'data': 'err'})
def jianchange(request):
    car_id = int(request.GET.get('car_id'))
    if  Usercar.objects.filter(car_co=car_id).exists():
        number = Usercar.objects.filter(car_co=car_id).values()[0]["car_number"]
        us = Usercar.objects.get(car_co=car_id)
        co = Commodity.objects.get(co_id=car_id)
        if number > 1:
            number -= 1
            co.co_number = co.co_number + 1
            co.save()
            us.car_number = number
            us.save()
            return JsonResponse({'data': number})
        elif number>0:
            co.co_number = co.co_number + 1
            co.save()
            us.delete()
            return JsonResponse({'data': 0})
        else:
            return JsonResponse({'data': 0})
    else:
        return JsonResponse({'data': 0})
def car(request):
    commoditylist = Commodity.objects.filter(co_kind=4)
    return render(request,'myapp/car.html',{'title':'购物车','commoditylist':commoditylist})
def mean(request):
    return render(request,'myapp/mean.html',{'title':'我的'})
def register(request):
    return render(request, 'myapp/register.html')
def sign(request):
    return render(request, 'myapp/sign.html')




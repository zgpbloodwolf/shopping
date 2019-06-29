from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
from django.conf import settings
import time
import re
from .models import Rotation,Menu,Commodity_kind,Commodity,Jdmsb,Fxhhb,Ppmsb,Hmzjb,Usercar,Order
from .models import Userinform
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
#商品列表
def kenview(request):
    comp = request.GET.get('aa')
    compID = Commodity_kind.objects.filter(ct_name=comp).values()[0]['ct_id']
    list=[]
    token = request.session.get('token')
    if token !=None:
        username = Userinform.objects.get(token = token).username
    else:
        username = '1'
    commoditylist = Commodity.objects.filter(co_kind=compID)
    for commodity in commoditylist:
        if Usercar.objects.filter(car_co=commodity.co_id,car_user=username).exists():
            number = Usercar.objects.filter(car_co=commodity.co_id,car_user=username).values()[0]['car_number']
            list.append([commodity.co_image, commodity.co_pice, commodity.co_brief_introduction, commodity.co_id, number])
        else:
            list.append([commodity.co_image,commodity.co_pice,commodity.co_brief_introduction,commodity.co_id,0])
    return JsonResponse({'data':list})
#增加购物车
def addchange(request):
    token = request.session.get('token')
    if token !=None:
        user = Userinform.objects.get(token=token)
        car_id = int(request.GET.get('car_id'))
        co = Commodity.objects.get(co_id=car_id)
        if not Usercar.objects.filter(car_co=car_id,car_user=user.username).exists():
            usercar = Usercar()
            #用户
            usercar.car_user = user.username
            #商品id
            usercar.car_co = car_id
            #数量
            usercar.car_number = 1
            #选中状态
            usercar.car_sele = 1
            #价格
            usercar.car_money = Commodity.objects.filter(co_id=car_id).values()[0]["co_pice"]
            #图片
            usercar.car_image = Commodity.objects.filter(co_id=car_id).values()[0]["co_image"]
            #简介
            usercar.co_brief_introduction=Commodity.objects.filter(co_id=car_id).values()[0]["co_brief_introduction"]
            usercar.save()
            co.co_number = co.co_number - 1
            co.save()
            return JsonResponse({"data":1})
        else:
            maxnumber = Commodity.objects.filter(co_id=car_id).values()[0]["co_number"]
            number = Usercar.objects.filter(car_co=car_id,car_user=user.username).values()[0]["car_number"]
            if maxnumber > 0:
                number += 1
                us = Usercar.objects.get(car_co=car_id,car_user=user.username)
                co.co_number = co.co_number - 1
                co.save()
                us.car_money=co.co_pice*number
                us.car_number = number
                us.save()
                picelist = Usercar.objects.values()
                maxpice = 0
                for pice in picelist:
                    if pice['car_sele']:
                        maxpice += pice['car_money']
                return JsonResponse({'data': number,'danjia':us.car_money,'zj':maxpice})
            else:
                return JsonResponse({'data': 'err'})
    else:
        return JsonResponse({'data': 'error'})
#减少购物车
def jianchange(request):
    token = request.session.get('token')
    if token != None:
        user = Userinform.objects.get(token=token)
        car_id = int(request.GET.get('car_id'))
        if  Usercar.objects.filter(car_co=car_id,car_user=user.username).exists():
            number = Usercar.objects.filter(car_co=car_id,car_user=user.username).values()[0]["car_number"]
            us = Usercar.objects.get(car_co=car_id,car_user=user.username)
            co = Commodity.objects.get(co_id=car_id)
            number -= 1
            if number > 0:
                us.car_money = co.co_pice * number
                us.car_number = number
                us.save()
            else:
                us.delete()
            co.co_number = co.co_number + 1
            co.save()
            picelist = Usercar.objects.values()
            maxpice = 0
            for pice in picelist:
                if pice['car_sele']:
                    maxpice += pice['car_money']
            return JsonResponse({'data': number,'zj':maxpice,'danjia':us.car_money})
        else:
            return JsonResponse({'data': 0})
    else:
        return JsonResponse({'data': 'error'})
#购物车
def car(request):
    token = request.session.get('token')
    username = Userinform.objects.get(token=token).username
    carlist = Usercar.objects.filter(car_user=username)
    picelist = Usercar.objects.filter(car_user=username).values()
    maxpice = 0
    for pice in picelist:
        if pice['car_sele']:
            maxpice += pice['car_money']
    return render(request,'myapp/car.html',{'title':'购物车','carlist':carlist,'maxpice':maxpice})
#改变选择状态
def chosenchange(request):
    token = request.session.get('token')
    username = Userinform.objects.get(token=token).username
    coid = int(request.GET.get('co_id'))
    carlist = Usercar.objects.get(car_co=coid,car_user=username)
    if carlist.car_sele:
        carlist.car_sele = 0
    else:
        carlist.car_sele = 1
    carlist.save()
    return  JsonResponse({'data':1})
#选好物品结算
def jiesuan(request):
    #购买商品列表
    token = request.session.get['token']
    username = Userinform.objects.get(token=token).username
    colist = Usercar.objects.filter(car_sele=1,car_user=username).values()
    for co in colist:
        new_order = Order()
        new_order.car_user = co['car_user']
        new_order.car_co = co['car_co']
        new_order.car_number = co['car_number']
        new_order.car_money = co['car_money']
        new_order.car_image=co['car_image']
        new_order.co_brief_introduction = co['co_brief_introduction']
        new_order.or_sele = 0
        new_order.or_evaluate = 0
        new_order.save()
        de_co = Usercar.objects.get(car_co=co['car_co'])
        de_co.delete()
    return JsonResponse({'code':1})
#我的
def mean(request):
    username = request.session.get('username','未登录')
    token = request.session.get('token')
    if token !=None:
        us = Userinform.objects.get(token=token)
        userimg = us.user_head
    else:
        userimg=''
    return render(request, 'myapp/mean.html', {'title': '我的', 'username': username, 'userimg': userimg})
import os
#注册
def register(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        userpassword = request.POST.get('password')
        userphone = request.POST.get('phone')
        token = str(time.time())+username
        user_head = request.FILES.get('head')
        hepath =  './static/upfile/'+username+'.png'
        with open(hepath,'wb') as f:
            for ini in user_head.chunks():
                f.write(ini)
        user = Userinform()
        user.username= username
        user.userpassword = userpassword
        user.userphone = userphone
        user.token = token
        user.user_head = hepath
        user.save()
        request.session['username']=username
        request.session['token'] = token
        return redirect('app:mean')

    else:
        return render(request, 'myapp/register.html')
#登录
def sign(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        if Userinform.objects.filter(username=username):
           us = Userinform.objects.get(username=username)
           if us.userpassword == password:
               us.token = str(time.time())+username
               us.save()
               request.session['username'] = username
               request.session['token'] = us.token
               return redirect('app:mean')
           else:
               pass
        else:
            pass
        return render(request, 'myapp/sign.html',{'error':'登录失败'})
    else:
        return render(request, 'myapp/sign.html')
#待收货
def toreceived(request):
    torelist = Order.objects.filter(or_sele=0)
    return render(request, 'myapp/toreceived.html',{'torelist':torelist})
#确认收货
def queren(request):
    co_id = int(request.GET.get('co_id'))
    co = Order.objects.get(car_co=co_id)
    co.or_sele = 1
    co.save()
    return JsonResponse({'data':1})
#用户验证
def verusername(request):
    username = request.POST.get('usrname')
    if Userinform.objects.filter(username=username):
        return JsonResponse({'data': '该用户已被注册', 'sta': 'error'})
    else:
        return JsonResponse({'data': '可以注册', 'sta': 'success'})
from django.contrib.auth import logout
def quite(request):
    logout(request)
    return redirect('app:mean')








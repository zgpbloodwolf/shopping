from django.db import models
from tinymce.models import HTMLField
# Create your models here.
#商品种类 如水果，服装等
class Commodity_kind(models.Model):
    ct_id = models.IntegerField(primary_key=True)
    ct_name= models.CharField(max_length=10)
    class Meta:
        db_table = 'commodity_kind'
    def __str__(self):
        return self.ct_name
#商品类： id 名字 价格  数量 图片 种类 简介
class Commodity(models.Model):
    co_id = models.IntegerField(primary_key=True)
    co_name = models.CharField(max_length=50)
    co_pice = models.DecimalField(max_digits=10,decimal_places=2)
    co_number = models.IntegerField()
    co_image = models.CharField(max_length=50)
    co_kind = models.IntegerField()
    co_brief_introduction = models.CharField(max_length=50)
    class Meta:
        db_table = 'commodity'
    def __str__(self):
        return self.co_name
#商品图片展示 图片id 路径 对应商品
class Commodity_img(models.Model):
    ci_id = models.IntegerField(primary_key=True)
    ci_img = models.ImageField()
    ci_co = models.IntegerField()
    class Meta:
        db_table = 'commodity_img'
#商品简介
class Commodity_brief_introduction(models.Model):
    id = models.AutoField(primary_key=True)
    cbi = models.TextField()
    cbi_co = models.IntegerField()
    class Meta:
        db_table = 'commodity_brief_introduction'
#轮播图 id 图片 对应商品
class Rotation(models.Model):
    ro_id = models.AutoField(primary_key=True)
    ro_image= models.ImageField()
    ro_co = models.IntegerField()
    class Meta:
        db_table = 'rotation'
    def __str__(self):
        return self.ro_image
#特殊商品展示菜单
class Menu(models.Model):
    m_id=models.IntegerField(primary_key=True)
    m_image = models.ImageField()
    m_name = models.CharField(max_length=20)
    m_co = models.IntegerField()
    class Meta:
        db_table = 'menu'
#秒杀
class Jdmsb(models.Model):
    jdms_image= models.ImageField()
    jdms_pice=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        db_table = 'jdms'
#发现好货
class Fxhhb(models.Model):
    fxhh_image= models.ImageField()
    fxhh_pice=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        db_table = 'fxhh'
#品牌秒杀
class Ppmsb(models.Model):
    ppms_image= models.ImageField()
    ppms_name=models.CharField(max_length=20)
    class Meta:
        db_table = 'ppms'
#会买专辑
class Hmzjb(models.Model):
    hmzj_image= models.ImageField()
    hmzj_pice=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        db_table = 'hmzj'
#用户信息
class Userinf(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    userpassword= models.CharField(max_length=15)
    userphone = models.IntegerField()
    token = models.CharField(max_length=50)
    class Meta:
        db_table = 'userin'
#购物车
class Usercar(models.Model):
    car_user = models.CharField(max_length=20)
    car_co = models.IntegerField()
    car_number = models.IntegerField()
    #选中状态
    car_sele = models.IntegerField()
    #商品价格
    car_money = models.DecimalField(max_digits=10,decimal_places=2)















from django.contrib import admin
from .models import Rotation,Commodity,Commodity_kind,Commodity_img,Commodity_brief_introduction
# Register your models here.
#关联表
# class sth(admin.TabularInline):
#     model= 类名
#     extra = 2
@admin.register(Rotation)
class RotationAdmin(admin.ModelAdmin):
    list_display = ['ro_id', 'ro_image', 'ro_co']
    list_per_page = 5
@admin.register(Commodity_brief_introduction)
class Commodity_brief_introductionAdmid(admin.ModelAdmin):
    list_display = ['id', 'cbi', 'cbi_co']
    list_per_page = 5
@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ['co_id', 'co_name','co_pice','co_number','co_image','co_kind','co_brief_introduction']
    list_per_page = 5
@admin.register(Commodity_img)
class Commodity_imgAdmin(admin.ModelAdmin):
    list_display = ['ci_id','ci_img','ci_co']
    list_per_page = 5
@admin.register(Commodity_kind)
class Commodity_kindAdmin(admin.ModelAdmin):
    list_display = ['ct_id', 'ct_name']
    list_per_page = 5
# class GradeAdmin(admin.ModelAdmin):
#     #列表页属性
#     #页面显示
#     # list_display = ['pk','gname','gdate','ggirlnum']
#     #过滤器
#     # list_filter = ['gname']
#     #搜索
#     # search_fields = ['gname']
#     #分页
#     list_per_page = 5
#     # #添加修改页属性
#     #属性的先后顺序
#     # fields = []
#     #给属性分组
#     # fieldsets = []
# admin.site.register(Commodity_brief_introduction,Commodity_brief_introductionAdmid)

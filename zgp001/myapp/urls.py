from django.conf.urls import url
from . import views
app_name='app'
urlpatterns = [
    url('^main/$',views.main,name='main'),
    url('^ken/$',views.ken,name='ken'),
    url('^car/$',views.car,name='car'),
    url('^mean/$',views.mean,name='mean'),
    url('^sign/$',views.sign,name='sign'),
    url('^register/$',views.register,name='register'),
    url('^aaa/$',views.kenview,name='aaa'),
    url('^addchange/$',views.addchange,name='addchange'),
    url('^jianchange/$',views.jianchange,name='jianchange'),
    url('^chosenchange/$',views.chosenchange,name='chosenchange'),
    url('^jiesuan/$',views.jiesuan,name='jiesuan'),
    url('^toreceived/$',views.toreceived,name='toreceived')
    # url('main/[A-Za-z_0-9]{0.9}.jpg/$',views.pic)
]
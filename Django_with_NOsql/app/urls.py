from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('index/insert/',views.insert,name='insert'),
    path('index/insert/insertdata/',views.insertdata,name='insertdata'),
    
    path('index/select/',views.select,name='select'),
    path('index/select/selectdevid/',views.selectdevid,name='selectdevid'),
    path('index/select/selectdevid/selectone/',views.selectone,name='selectone'),
    path('index/select/selectdevid/selectall/',views.selectall,name='selectall'),
    
    path('index/update/',views.update,name='update'),
    path('index/update/updatedata/',views.updatedata,name='updatedata'),
    
    path('index/delete/',views.delete,name='delete'),
    path('index/select/deletedevid/',views.deletedevid,name='deletedevid'),
    path('index/delete/deletedevid/deleteone/',views.deleteone,name='deleteone'),
    path('index/select/deletedevid/deleteall/',views.deleteall,name='deleteall'),
    
    ]
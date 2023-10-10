from django.urls import path,include
from . import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('index/insert/',views.insert,name='insert'),
    path('index/insert/insertoption/',views.insertoption,name='insertoption'),
    
    path('index/insert/insertoption/insertdata_customers_success/',views.insertdata_customers_success,name='insertdata_customers_success'),
    path('index/insert/insertoption/insertdata_customers_success/insertdata_customers_again',views.insertdata_customers_again,name='insertdata_customers_again'),
    
    # path('index/insert/insertoption/employees/',views.insertoption,name='employees'),
    # path('index/insert/insertoption/products/',views.insertoption,name='products'),
    # path('index/insert/insertoption/bill/',views.insertoption,name='bill'),
    path('test/',views.test,name='test'),
    
    
    
    # ####
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


# https://docs.djangoproject.com/en/dev/ref/templates/language/#template-inheritance
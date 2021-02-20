"""FoodOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from FoodApp import views
urlpatterns = [
    path('admin', admin.site.urls),
    path('sign/',views.signup,name='signup'),
    path('',views.product_list.as_view(),name='list'),
    path('detail/<pk>',views.product_detail.as_view(),name='detail'),
    path('delete/<a>',views.delcart),
    path('del/<a>',views.delhis),
    path('cart',views.viewcart,name='cart'),
    path('addcart',views.addcart),
    path('update',views.updatecart),
    path('test',views.test,name='test'),
    path('orders',views.ordertab,name='orders'),
    path('orderhis',views.orderhis,name='orderhis'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('check',views.CheckUser),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

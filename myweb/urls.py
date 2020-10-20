"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myapp import views # 在这里添加这一行代码，导入 views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),    # 在这里添加这一行代码，这是我们上一步编写的视图函数的路由，默认是 / 路径
    path('index', views.index),    # 在这里添加这一行代码，这是我们上一步编写的视图函数的路由，默认是 / 路径
    path('search', views.search),
    path('doSearch', views.doSearch),
    path('execute', views.execute),
    path('doExecute', views.doExecute),

]

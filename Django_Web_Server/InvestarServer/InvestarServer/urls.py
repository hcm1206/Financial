"""
URL configuration for InvestarServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from hello import views
from django.urls import path, re_path
from index import views as index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 정규 표현식을 이용해 hello 애플리케이션의 sayHello 뷰 URL 처리
    re_path(r'^(?P<name>[A-Z][a-z]*)$', views.sayHello),
    # index 애플리케이션 뷰의 main_view() 함수로 매핑하는 URL 처리
    path('index/', index_views.main_view),
]

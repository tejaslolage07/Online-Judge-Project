"""OnlineJudge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from OJ import views
from django.conf.urls.static import static
from django.conf import settings

# app_name = 'OJ'
# path('', include(('OJ.urls', 'OJ'), namespace='OJ'))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage, name="Login"),
    path('logout/', views.logoutUser, name="Logout"),
    path('register/', views.Registration, name="Registration"),
    path('problems/', views.problemsList, name="Problems"),
    path('problems/<int:id>/', views.problemDetails, name="Details"),
    path('problems/<int:id>/code/', views.codeSubmission, name="Code"),
    path('problems/<int:id>/code/verdict/',
         views.judgeVerdict, name="Verdict"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

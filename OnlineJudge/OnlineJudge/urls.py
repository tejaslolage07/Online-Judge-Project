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

app_name = 'OJ'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_signup.as_view(), name="Login"),
    path('problems/', views.ProblemsList.as_view(), name="Problems"),
    path('problems/<int:pk>/', views.ProblemDetails.as_view(), name="Details"),
    path('problems/<int:pk>/code/', views.CodeSubmission.as_view(), name="Code"),
    path('problems/<int:pk>/code/verdict/', views.JudgeVerdict.as_view(), name="Verdict"),
]

"""foodapp URL Configuration

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
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls import url, include
"""
from .FolderName.FileName import ClassName

upper statement means import a class from a file which exist in a folder 

.			=>	current Folder where urls.py reside
FolderName	=>	Controllers is a folder name
FileName	=>	MyClass is a file which exists in Controllers folder as MyClass.py
ClassName	=>	MyClass is Python class which syntax exists in MyClass.py

"""
from .Controllers import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<int:question_id>/', myclass.MyClass().detail, name='detail'),
    path('', UserController.UserController().userDashboard, name='userDashboard'),
    path('register', UserController.UserController().userSignup, name='userSignup'),
    path('loginrd', UserController.UserController().userLoginRd, name='userLoginRd'),
    path('login', UserController.UserController().userLogin, name='userLogin'),
    path('logout', UserController.UserController().userLogout, name='userLogout'),

    #Currency APIs
    path('currencies/', CurrencyApiController.CurrencyApiController.allCurrency, name='allCurrency'),
    path('addcurrency/', CurrencyApiController.CurrencyApiController.addCurrency, name='addCurrency'),
    path('getcurrency/', CurrencyApiController.CurrencyApiController.getCurrency, name='getCurrency'),
    path('updatecurrency/', CurrencyApiController.CurrencyApiController.updateCurrency, name='updateCurrency'),
    path('removecurrency/', CurrencyApiController.CurrencyApiController.removeCurrency, name='removeCurrency'),

    #Conversion APIs
    path('conversions/', ConversionApiController.ConversionApiController.allConversions, name='allConversions'),
    path('addconversion/', ConversionApiController.ConversionApiController.addConversion, name='addConversion'),
    path('getconversion/', ConversionApiController.ConversionApiController.getConversion, name='getConversion'),
    path('getconversionrate/', ConversionApiController.ConversionApiController.getConversionRate, name='getConversionRate'),
    path('updateconversion/', ConversionApiController.ConversionApiController.updateConversion, name='updateConversion'),
    path('removeconversion/', ConversionApiController.ConversionApiController.removeConversion, name='removeConversion'),

    #Currency Web Interface
    path('currencies', CurrencyController.CurrencyController().allCurrencies, name='allCurrencies',),
    path('currency', CurrencyController.CurrencyController().addUpdateCurrency, name='addUpdateCurrency',),
    path('currency/<int:c_id>/', CurrencyController.CurrencyController().addUpdateCurrency, name='addUpdateCurrency',),
    path('removecurrency/<int:c_id>/', CurrencyController.CurrencyController().removeCurrency, name='removeCurrency',),

    #Auth APIs
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth-get-jwt-token/', obtain_jwt_token, name='api_auth_get_jwt_token'),
    path('api-auth-refresh-jwt-token/', refresh_jwt_token, name='api_auth_refresh_jwt_token'),

]

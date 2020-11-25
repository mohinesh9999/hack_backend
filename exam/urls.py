from rest_framework_simplejwt import views as jwt_views 
from django.urls import path,include
from django.contrib import admin
from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import exam
from .views import *
urlpatterns = [
    path('addqn/', 
         addqn.as_view(), 
         name ='addqn'),
    path('addtest/', 
         addtest.as_view(), 
         name ='addtest'),
    path('testlogin/', 
         testlogin.as_view(), 
         name ='testlogin'),
]
urlpatterns += staticfiles_urlpatterns()
# urlpatterns += patterns('',
#  (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#  )
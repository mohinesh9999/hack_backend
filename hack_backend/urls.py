from rest_framework_simplejwt import views as jwt_views 
from django.urls import path,include
from django.contrib import admin
from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import exam
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', 
         jwt_views.TokenObtainPairView.as_view(), 
         name ='token_obtain_pair'), 
    path('api/token/refresh/', 
         jwt_views.TokenRefreshView.as_view(), 
         name ='token_refresh'), 
    path('exam/', include('exam.urls')),

]
urlpatterns += staticfiles_urlpatterns()
# urlpatterns += patterns('',
#  (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#  )
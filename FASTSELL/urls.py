# myproject/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),  
    path('ai_api/', include('ai_api.urls')),  
]

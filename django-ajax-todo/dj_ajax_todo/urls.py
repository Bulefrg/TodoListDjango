from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('',include('todo.urls')),
    path('todos/',include('todo.urls')),
    path('admin/', admin.site.urls),
]

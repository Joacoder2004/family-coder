from django.contrib import admin
from django.urls import path
from tarea.views import hola
from tarea.views import family
urlpatterns = [
    path('admin', admin.site.urls),
    path('HolaMundo',hola),
    path('family', family)
]

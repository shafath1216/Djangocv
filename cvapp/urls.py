from django.urls import path,include
from .views import index,preview_cv

urlpatterns = [
    path('',index,name='index'),
    path('preview_cv/',preview_cv,name='preview_cv')
]


from django.urls import path
from imageapp import views

urlpatterns = [
    path('', views.home),
    path('addimage',views.image_save),
    path('showimage',views.image_show,name='showimage') ,
    path('success', views.success, name='success'),
]
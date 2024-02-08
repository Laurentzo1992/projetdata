from  django.urls import  path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict_model', views.predict_model, name='predict_model'),
]




    
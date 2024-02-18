from django.urls import path
from . import views
urlpatterns = [
   path('', views.ma_vue, name='receive_ttn_data'), 

]

from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('drink_list',views.drink_list,name="drink_list"),
    path('drink/<int:id>',views.drink_details)
]
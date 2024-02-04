from django.urls import path
from . import views


urlpatterns = [
    path('', views.generations, name='generations'),
    path('start-generation', views.start_generation, name='start-generation'),
    path('check-generation/<int:generation_id>', views.check_generation, name='check-generation'),
    path('complete-generation/<str:secret_key>', views.complete_generation, name='complete-generation'),
]


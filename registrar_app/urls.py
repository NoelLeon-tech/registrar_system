from django.urls import include, path
from . import views

urlpatterns = [
    path('queue_list', views.queue_list, name='queue_list'),
    path('new_queue', views.new_queue, name='new_queue')
]
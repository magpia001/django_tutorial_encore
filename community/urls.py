from django.urls import path
from community.views import write, articleList, viewDetail

urlpatterns = [
    path('write/', write, name='write'),
    path('list/', articleList, name='list'),
    path('view_detail/<int:num>/', viewDetail, name='view_detail'),
]
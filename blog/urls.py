from django.urls import path
from .views import post_create,post_list,post_detail,post_update,post_delete,post_like
urlpatterns = [
    path('post-create/', post_create, name='post_create'),
    path('post-list/', post_list, name='post_list'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:slug>/update/', post_update, name='post_update'),
    path('<slug:slug>/delete/', post_delete, name='post_delete'),
    path('<slug:slug>/like/', post_like, name='post_like'),

    
]
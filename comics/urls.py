from django.urls import path
from .views import comic_list, comic_detail, comic_create, comic_update, comic_delete

urlpatterns = [
    path('', comic_list, name='comic_list'),
    path('<int:pk>/', comic_detail, name='comic_detail'),
    path('create/', comic_create, name='comic_create'),
    path('<int:pk>/update/', comic_update, name='comic_update'),
    path('<int:pk>/delete/', comic_delete, name='comic_delete'),
]
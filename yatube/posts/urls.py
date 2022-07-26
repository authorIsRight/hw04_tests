from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    # Профайл пользователя
    path('profile/<str:username>/', views.profile, name='profile'),

    # Просмотр записи
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/edit/', views.post_edit, name="post_edit"),
    path('create/', views.post_create, name='post_create'),
    # comment
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def root_redirect(request):
    return redirect('comic_list')  # 这里的 'comic_list' 是你在 comics.urls 中定义的 comic_list 视图的名称

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comics/', include('comics.urls')),
    path('', root_redirect, name='root_redirect'),
]

# 仅在开发环境下添加媒体文件的 URL 映射
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
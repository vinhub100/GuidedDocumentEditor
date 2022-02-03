
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView
from Editor.views import MainHome, MainArticleDetail

urlpatterns = [
    path('',MainHome, name='main-home'),
    re_path(r'editor[/]', include('Editor.urls')),
    path('login', LoginView.as_view(template_name='editor/login.html',redirect_authenticated_user='/editor/')),
    path('logout', LogoutView.as_view(next_page='/')),
    path('admin/', admin.site.urls),
    path('article/<slug:slug>', MainArticleDetail, name="article-detail"),
    re_path(r'article[/]', RedirectView.as_view(url='/', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

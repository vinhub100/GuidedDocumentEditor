from django.urls import path
from .views import home, drafts, create, add_image, image_store, show_article, update


urlpatterns = [
    path('', home),
    path('drafts',drafts),
    path('create', create, name='createBlog'),
    path('blog/<slug:slug>/update', update, name='updatearticle'),
    path('blog/<slug:slug>', show_article, name='showarticle'),
    path('image_store', image_store, name='imagestore'),
    path('image_upload', add_image, name='addimage'),
]

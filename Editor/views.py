import time
import datetime
import json
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django import http
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from http import HTTPStatus
from .models import Article, Photos
from .pagegen import render_body, update_body


def MainHome(request):
    try:
        articles = Article.objects.filter(a_type='P').order_by('-creation_date')
        paginator = Paginator(articles, 16)
        page = request.GET.get('page')
        paged_article = paginator.get_page(page)
        if len(paged_article) == 0:
            paged_article = 0
    except Exception as ex:
        print(type(ex))
        paged_article = None
    return render(request,'main/home.html',{'articles':paged_article})

def MainArticleDetail(request, slug):
    artl = get_object_or_404(Article,slug=slug,a_type='P')
    try:
        rec = Article.objects.filter(a_type='P').order_by('-creation_date')[:4]
        rec_len = len(rec)
    except Exception:
        rec_len = 0
    bdy = json.loads(artl.body)
    htm = render_body(bdy)
    return render(request,'main/article.html',{'article': artl, 'body': htm, 'rec':rec, 'rec_len':rec_len})


@login_required
def home(request):
    try:
        articles = Article.objects.filter(a_type='P',author= request.user).order_by('-creation_date')
        paginator = Paginator(articles, 15)
        page = request.GET.get('page')
        paged_article = paginator.get_page(page)
        if len(paged_article) == 0:
            paged_article = 0
    except Exception as ex:
        print(type(ex))
        paged_article = None
    return render(request, 'editor/list_article.html', { "label":"Published Articles","articles":paged_article })


@login_required
def show_article(request, slug):
    artl = get_object_or_404(Article,slug=slug)
    bdy = json.loads(artl.body)
    htm = render_body(bdy)
    return render(request, 'editor/show_article.html', {'article': artl, 'body': htm})

@login_required
def drafts(request):
    try:
        articles = Article.objects.filter(a_type='D',author= request.user).order_by('-creation_date')
        paginator = Paginator(articles, 15)
        page = request.GET.get('page')
        paged_article = paginator.get_page(page)
        if len(paged_article) == 0:
            paged_article = 0
    except Exception as ex:
        print(type(ex))
        paged_article = None
    return render(request, 'editor/list_article.html', { "label":"Drafts", "articles":paged_article })

@login_required
@csrf_exempt
def create(request):
    if request.method == "POST":
        article = Article()
        dt = json.loads(request.body)
        article.heading = dt["heading"]
        article.discription = dt["discription"]
        article.dp = dt["dp"]
        article.a_type = dt["a_type"]
        article.body = dt["body"]
        article.author = request.user
        article.save()
        return redirect("/")
    return render(request, 'editor/create.html', {})


@login_required
@csrf_exempt
def update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        dt = json.loads(request.body)
        article.heading = dt["heading"]
        article.discription = dt["discription"]
        article.dp = dt["dp"]
        article.a_type = dt["a_type"]
        article.body = dt["body"]
        article.save()
        return redirect("/")
    bdy = json.loads(article.body)
    htm = update_body(bdy)
    return render(request, 'editor/update.html', {'article': article, 'body':htm})

@xframe_options_sameorigin
@login_required
def image_store(request):
    try:
        poto = Photos.objects.all().order_by("-date")
        paginator = Paginator(poto, 15)
        page = request.GET.get('page')
        images = paginator.get_page(page)
    except Exception:
        images = None
    return render(request, 'editor/image_store.html', {'images':images})

@xframe_options_sameorigin
@login_required
def add_image(request):
    if request.method == "POST":
        poto = Photos()
        poto.discription = request.POST.get('discription', None)
        poto.date = time.strftime('%Y-%m')
        poto.image = request.FILES.get('image', None)
        poto.save()
        return redirect('imagestore')
    return render(request, 'editor/image_upload.html', {})


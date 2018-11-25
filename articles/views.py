from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# view on article page
def article_list(request):
    # order all objects by date field
    articles = Article.objects.all().order_by('date')
    # use app template for viewing, and send the ordered data (as a dictionary)
    return render(request,'articles/article_list.html',{'articles':articles})

# view for each article
def article_detail(request, slug):
    # all info about one article object
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

# view for create an article object
@login_required(login_url="/accounts/login/") # decorator for requiring login to create
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            article_instance = form.save(commit=False)
            article_instance.author = request.user
            article_instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html',{'form':form})

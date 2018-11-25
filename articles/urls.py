from django.urls import path
from . import views

# url namespace
app_name = 'articles'

urlpatterns = [
    # direct path to something in app view
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name="create"),
    # capture "slug" and send to views
    path('<slug>/', views.article_detail, name="detail"),
]

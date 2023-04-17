from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('membros', views.membros, name='membros'),
    
    path('<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
]

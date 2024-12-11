from django.urls import path
from . import views


app_name = 'polls'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about, name="aboutpage"),
    path('',views.index,name='index'),
    path('<int:qstn_id>/', views.detail, name='detail'),
    path('<int:qstn_id>/', views.result,name='result'),
    path('<int:qstn_id>',views.vote,name='vote'),
    ]  
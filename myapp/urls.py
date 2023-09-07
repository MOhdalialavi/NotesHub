
from . import  views
from django.urls import path,re_path


urlpatterns=[
 
    path('',views.index,name='home'),
    path('login/', views.login,name='login'),
    path('admin/', views.admin_view, name='admin'),
    path('', views.logout_view, name='logout'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^category/(?P<category_name>[a-zA-Z]+)/$', views.category_view, name='category'),
    re_path(r'^category/(?P<category_name>[a-zA-Z]+)/(?P<class_name>[-\w\s]+)/$', views.class_view, name='class'),
    re_path(r'^category/(?P<category_name>[a-zA-Z]+)/(?P<class_name>[-\w\s]+)/(?P<subject_name>[-\w\s]+)/$', views.board, name='board'),
]
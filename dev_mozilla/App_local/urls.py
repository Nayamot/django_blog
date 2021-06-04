from App_local import views
from django.urls import path
from App_local import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/',views.blogpost, name='blog'),
    path('blog/blog_detail/<int:blog_id>/',views.blog_detail,),
    path('blog/create_blog/', views.create_blog),
    path('blog/edit_blog/<int:pk>/', views.edit_blog),
    path('blog/delete_blog/<int:pk>/', views.delete_blog),




    path('contact/',views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('lalbag/', views.lalbag, name='lalbag'),
    path('mountainpakistan/', views.mountainpakistan, name='mountainpakistan'),
    path('pyramid_egypt/', views.pyramid_egypt, name='pyramid_egypt'),
]

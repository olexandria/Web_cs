from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^books/create/$', views.book_create, name='book_create'),
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest_librarys/',  views.list_librarys),
    url(r'^rest_library/(?P<code>\d+)/$', views.library_details),
    url(r'^rest_reader/', views.client),
    url(r'^rest_librarys/',  views.list_librarys),
    url(r'^rest_library/(?P<code>\d+)/', views.library_details),
    url(r'^rest_client', views.client, name='rest_client'),	
    url(r'^librarys', views.librarys, name='librarys'),	
    url(r'^booklist', views.books, name='booklist'),		
    url(r'^index', views.index, name='index'),  # index view at /
    url(r'^likepost/$', views.likePost, name='likepost'),   # likepost view at /likepost		

]
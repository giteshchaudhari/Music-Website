from django.conf.urls import url
from song import views

app_name='song'

urlpatterns=[
	url(r'^my_song/$',views.MyGeetList,name='my_geet_list'),
	url(r'^about/$',views.AboutView.as_view(),name='about'),
	url(r'^geet/new/$',views.CreateGeetView,name='geet_new'),
	url(r'^geet/(?P<pk>\d+)/delete/$',views.GeetDeleteView,name='geet_delete'),
	url(r'^geet/(?P<pk>\d+)/favourite/$',views.Favourite,name='geet_fav'),
] 
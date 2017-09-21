from django.conf.urls import url
from .import views
from blog.views import post_add

app_name = 'blog'

urlpatterns = [
    #/blog/
    url(r'^$',views.index,name='index'),

    #/blog/posts/
    url(r'^posts/$',views.PostView.as_view(),name='posts'),

    #/blogs/post/add/
    url(r'^posts/add/$',post_add,name='post_add'),

    #/blog/posts/712/
    url(r'^post/(?P<pk>[0-9]+)/detail/$',views.DetailView.as_view(),name='detail'),

    #/blog/post/update/
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.PostUpdate.as_view(),name='post_update'),

    #/blog/post/delete/
    url(r'^post/(?P<pk>[0-9]+)/delete/$',views.PostDelete.as_view(),name='post_delete'),

    #/blog/register
    url(r'^register/$',views.UserFormView.as_view(),name='register'),

    #/blog/login
    url(r'^login/$',views.UserLoginView.as_view(),name='login'),

    #/blog/logout
    url(r'^logout/$',views.logout_view,name='logout'),
]
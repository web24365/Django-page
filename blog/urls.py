from django.conf.urls import url
from . import views


urlpatterns = [
    # ^문자열의 시작, $문자열의 끝 사이에 아무것도 없는 것.
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
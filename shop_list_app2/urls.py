from django.conf.urls import patterns, url
from shop_list_app2.api import UserListAPI, ProductListAPI, UserDetailAPI, ProductDetailAPI


urlpatterns = patterns('',

    # URLS del API REST
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='api_user_list'),
    url(r'^api/1.0/user/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='api_user_detail'),
    url(r'^api/1.0/products/$', ProductListAPI.as_view(), name='api_photo_list'),
    url(r'^api/1.0/product/(?P<pk>[0-9]+)$', ProductDetailAPI.as_view(), name='api_photo_detail'),

)
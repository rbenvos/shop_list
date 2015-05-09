from django.conf.urls import patterns, url
from shop_list_app2.api import UserListAPI, ProductListAPI, UserDetailAPI, ProductDetailAPI
import views

urlpatterns = patterns('',

    url(r'^$', views.dashboard, name='dashboard'),

    #Menu
    url(r'^users/$', views.NewUserView.as_view(), name='users_list_view'),
    url(r'^groups/$', views.NewGroupView.as_view(), name='groups_list_view'),
    url(r'^devices/$', views.NewDeviceView.as_view(), name='devices_list_view'),
    url(r'^orders/$', views.NewOrderView.as_view(), name='orders_list_view'),
    url(r'^products/$', views.NewProductView.as_view(), name='products_list_view'),

    #Detalle
    url(r'^users/(?P<pk>[0-9]+)$', views.user_detail_view, name='user_detail_view'),
    url(r'^groups/(?P<pk>[0-9]+)$', views.group_detail_view, name='group_detail_view'),
    url(r'^devices/(?P<pk>[0-9]+)$', views.device_detail_view, name='device_detail_view'),
    url(r'^orders/(?P<pk>[0-9]+)$', views.order_detail_view, name='order_detail_view'),
    url(r'^products/(?P<pk>[0-9]+)$', views.product_detail_view, name='product_detail_view'),

    # URLS del API REST
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='api_user_list'),
    url(r'^api/1.0/user/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='api_user_detail'),
    url(r'^api/1.0/products/$', ProductListAPI.as_view(), name='api_photo_list'),
    url(r'^api/1.0/product/(?P<pk>[0-9]+)$', ProductDetailAPI.as_view(), name='api_photo_detail'),

)
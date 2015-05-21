from django.conf.urls import patterns, url
from shop_list_app2.api import UserListAPI, ProductListAPI, UserDetailAPI, ProductDetailAPI, UserDetailSimpleAPI,\
    GroupDetailAPI, GroupListAPI, PhoneDetailAPI, PhoneListAPI, \
    OrderDetailAPI, OrderListAPI, ItemDetailAPI, ItemListAPI
import views

urlpatterns = patterns('',

    url(r'^$', views.dashboard, name='dashboard'),

    #List
    url(r'^users/$', views.NewUserView.as_view(), name='users_list_view'),
    url(r'^groups/$', views.NewGroupView.as_view(), name='groups_list_view'),
    url(r'^devices/$', views.NewDeviceView.as_view(), name='devices_list_view'),
    url(r'^orders/$', views.NewOrderView.as_view(), name='orders_list_view'),
    url(r'^items/$', views.items_list_view, name='items_list_view'),
    url(r'^products/$', views.NewProductView.as_view(), name='products_list_view'),

    #Detalle
    url(r'^users/(?P<pk>[0-9]+)$', views.user_detail_view, name='user_detail_view'),
    url(r'^groups/(?P<pk>[0-9]+)$', views.group_detail_view, name='group_detail_view'),
    url(r'^devices/(?P<pk>[0-9]+)$', views.device_detail_view, name='device_detail_view'),
    url(r'^orders/(?P<pk>[0-9]+)$', views.order_detail_view, name='order_detail_view'),
    url(r'^products/(?P<pk>[0-9]+)$', views.product_detail_view, name='product_detail_view'),
    
    #Borrar
    url(r'^users/(?P<pk>[0-9]+)/delete/$', views.user_delete_view, name='user_delete_view'),
    url(r'^groups/(?P<pk>[0-9]+)/delete/$', views.group_delete_view, name='group_delete_view'),
    url(r'^devices/(?P<pk>[0-9]+)/delete/$', views.device_delete_view, name='device_delete_view'),
    url(r'^orders/(?P<pk>[0-9]+)/delete/$', views.order_delete_view, name='order_delete_view'),
    url(r'^products/(?P<pk>[0-9]+)/delete/$', views.product_delete_view, name='product_delete_view'),

    # URLS del API REST
    url(r'^api/2.0/users/$', UserListAPI.as_view(), name='api_user_list'),
    url(r'^api/2.0/user/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='api_user_detail'),
    url(r'^api/2.0/user/(?P<pk>[0-9]+)/simple/$', UserDetailSimpleAPI.as_view(), name='api_user_detail_simple'),
    #url(r'^api/2.0/user/(?P<pk>[0-9]+)/devices/$', UserDevicesDetailAPI.as_view(), name='api_user_devices_detail'),
    #url(r'^api/2.0/user/(?P<pk>[0-9]+)/friends/$', UserFriendsDetailAPI.as_view(), name='api_user_friends_detail'),
    
    url(r'^api/2.0/groups/$', GroupListAPI.as_view(), name='api_group_list'),
    url(r'^api/2.0/group/(?P<pk>[0-9]+)$', GroupDetailAPI.as_view(), name='api_group_detail'),
    
    url(r'^api/2.0/devices/$', PhoneListAPI.as_view(), name='api_device_list'),
    url(r'^api/2.0/device/(?P<pk>[0-9]+)$', PhoneDetailAPI.as_view(), name='api_device_detail'),
    
    url(r'^api/2.0/orders/$', OrderListAPI.as_view(), name='api_order_list'),
    url(r'^api/2.0/order/(?P<pk>[0-9]+)$', OrderDetailAPI.as_view(), name='api_order_detail'),
    
    url(r'^api/2.0/items/$', ItemListAPI.as_view(), name='api_item_list'),
    url(r'^api/2.0/item/(?P<pk>[0-9]+)$', ItemDetailAPI.as_view(), name='api_item_detail'),

    url(r'^api/2.0/products/$', ProductListAPI.as_view(), name='api_product_list'),
    url(r'^api/2.0/product/(?P<pk>[0-9]+)$', ProductDetailAPI.as_view(), name='api_product_detail'),

)
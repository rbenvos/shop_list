from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'shop_list.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^shop_list/', include('shop_list_app.urls')),
    url(r'^shop_list2/', include('shop_list_app2.urls')),

]

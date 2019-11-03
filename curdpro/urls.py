from django.conf.urls import include, url
from django.contrib import admin
from curdapp import views

urlpatterns = [
   url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.main_page),
    url(r'^create/',views.product_insert_view),
    url(r'^retrieve/',views.product_retrieve_view),
    url(r'^update/',views.product_update_view),
    url(r'^delete/',views.product_delete_view)
]

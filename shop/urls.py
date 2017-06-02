from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.category, name='category'),
    url(r'^$', views.product, name='product'),
    url(r'^login/$', views.login, name='login'),
]
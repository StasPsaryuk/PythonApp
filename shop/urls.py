from django.conf.urls import url
import views

urlpatterns = [

    url(r'^category/(?P<slug>(.*))/$', views.category, name='category'),
    url(r'^product/(?P<slug>(.*))/$', views.product, name='product'),

    url(r'^basket/$', views.basket, name='basket'),
    url(r'^add_to_basket/$', views.add_to_basket, name='add_to_basket'),
    url(r'^delete_from_basket/$', views.delete_from_basket, name='delete_from_basket'),
    url(r'^finish/$', views.finish, name='finish'),
    url(r'^help/$', views.help, name='help'),
    url(r'^save-messages/$', views.help_mes, name='help-mes'),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile', views.index, name='index'),
]
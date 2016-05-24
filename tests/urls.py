from django.conf.urls import include, url
from django.contrib import admin

from tests import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('foo/', views.MyView.as_view(), name='class-view'),
    url('bar/', views.MyAPIView.as_view(), name='api-view'),
    url('spam/', views.MyAPIView, name='missing-as-view'),
    url('', views.my_view, name='function-view'),
]

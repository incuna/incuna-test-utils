from django.conf.urls import url

from . import views


urlpatterns = [
    url('foo/', views.MyView.as_view(), name='class-view'),
    url('bar/', views.MyAPIView.as_view(), name='api-view'),
    url('', views.my_view, name='function-view'),
]

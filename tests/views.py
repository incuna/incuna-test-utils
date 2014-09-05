from django.http import HttpResponse
from django.views.generic import TemplateView, View
from rest_framework.response import Response
from rest_framework.views import APIView


def my_view(request, *args, **kwargs):
    return HttpResponse('My page.')


class MyView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('My page too.')


class MyAPIView(APIView):
    def get(self, request, format=None):
        return Response({})


class MyTemplateView(TemplateView):
    template_name = 'page.html'

from django.http import HttpResponse


def my_view(request, *args, **kwargs):
    """A test view with the same __name__ as views.my_view."""
    return HttpResponse('My other page.')

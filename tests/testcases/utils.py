import django


def is_django_gte_19():
    return django.VERSION >= (1, 9)

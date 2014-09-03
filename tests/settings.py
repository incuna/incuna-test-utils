import dj_database_url


DATABASES = {
    'default': dj_database_url.config(
        default='postgres://localhost/test_utils',
    ),
}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
)
MIDDLEWARE_CLASSES=()
SECRET_KEY = 'test'

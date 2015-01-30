import dj_database_url


DATABASES = {
    'default': dj_database_url.config(
        default='postgres://localhost/test_utils',
    ),
}
INSTALLED_APPS = (
    'incuna_test_utils',

    'tests',

    'feincms.module.page',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
)
MIDDLEWARE_CLASSES = ()
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
ROOT_URLCONF = 'tests.urls'
SECRET_KEY = 'test'
FEINCMS_USE_PAGE_ADMIN = False

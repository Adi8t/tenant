from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-i3a&(!v4$syw8g)^)%6x0qf!964lv6@r0lzxhc_d%!(b)*73k='
DEBUG = True
ALLOWED_HOSTS = []

SHARED_APPS = [
    'django_tenants',
    'insta',  # Must be first
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Ensure shared and tenant apps are listed here
]

TENANT_APPS = [
    'tenant_app',  # Your tenant-specific app
    # Add any other tenant-specific apps here
]

INSTALLED_APPS = SHARED_APPS + TENANT_APPS


MIDDLEWARE = [
    
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'insta.middleware.TenantMiddleware',
]


ROOT_URLCONF = 'kins.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kins.wsgi.application'

# Database configuration for multi-tenancy
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'kanhasoft',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Database routers for multi-tenancy
DATABASE_ROUTERS = [
    'django_tenants.routers.TenantSyncRouter',
]

# Multi-tenancy settings
TENANT_MODEL = "insta.Client"  # The model where tenants are stored
TENANT_DOMAIN_MODEL = "insta.Domain"  # The model for tenant domains

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '82ef670c34cac4'
EMAIL_HOST_PASSWORD = '6fec54776832b2'
EMAIL_PORT = '2525'


"""
Django settings for meetingroom project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ja=@3imt@ei(-zyue!k$@#js0xw@v7f+d@gwxgo_kyif_a9gr_'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# registration的登录后的跳转路径
LOGIN_REDIRECT_URL = '/'
# registration的注册后的跳转路径
SIMPLE_BACKEND_REDIRECT_URL = '/accounts/login/'

INSTALLED_APPS = [
    'simpleui',
    # 'bootstrap4',
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_oss_storage',
    # 'jobs',
    'jobs.apps.JobConfig',
    'interview',
    # 'wangzhe',
    'rest_framework',
    'meetingroom.apps.UniversalManagerApp',
    # 'django_celery_beat',
    'dashboard',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 管理员可以增删查改 普通用户只能读
    ]
}

LOGGING = {
    'version': 1,  # 固定参数
    'disable_existing_loggers': False,  # 是否禁用已有的log
    'formatters': {  # filter和formatters都有默认配置 可以不用配置
        'simple': {  # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(lineno)d %(levelname)-8s %(message)s',
            # asctime年月日时分秒  name 哪个类 lineno多少行 levelname日志级别 message什么样的文本消息
        },
    },
    'handlers': {  # handlers定义日志的处理器(如何处理日志)，handler可以放在filter里面
        'console': {  # 往控制台输出
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {  # 发送到邮件 Add Handler for mail_admins for `warning` and above
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {  # 保存到文件
            # 'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'meetingroom.admin.log'),
        },
        'performance': {  # 保存到文件
            # 'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'meetingroom.performance.log'),
        },
    },

    'root': {  # 系统全局级别默认的日志记录器，属于loggers里的一种特殊的记录器
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },

    'loggers': {  # 定义了日志记录的处理类/对象，可以包括多个handler
        # "django_python3_ldap": {
        #     "handlers": ["console", "file"],
        #     "level": "DEBUG",
        # },

        "interview.performance": {  # 定义来自interview/performance.py的日志处理对象，它的__name__就是interview.performance
            "handlers": ["console", "performance"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379",
        'TIMEOUT': 60,  # default expire time per api call
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # r/w timeout in seconds
            # 'MAX_ENTRIES': 10000,
            # 'KEY_PREFIX': 'recruit-',
        }
    }
}

MIDDLEWARE = [
    # 'interview.performance.performance_logger_middleware',
    'interview.performance.PerformanceAndExceptionLoggerMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',  # 新增
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',  # 新增
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meetingroom.urls'

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

WSGI_APPLICATION = 'meetingroom.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'Business': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'business',
    #     'USER': 'root',
    #     'PASSWORD': '123456',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306'
    # },
}

# DATABASE_ROUTERS = ['settings.router.DatabaseRouter']
DATABASE_ROUTERS = ['settings.database_router.DatabaseAppsRouter']
#
DATABASE_APPS_MAPPING = {
    'wangzhe': 'Business'  # key是app名，value是DATABASES的key
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # 检测密码相似度过高
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # 设置密码最小长度
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # 纯数字密码不通过
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'




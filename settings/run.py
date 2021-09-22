from .base import *

ALLOWED_HOSTS = ['127.0.0.1', "*", "host.docker.internal"]

DEBUG = True

## 钉钉通知
DINGTALK_WEB_HOOK = ''

# CDN的域名 http://cdn.xx.online
# STATIC_URL = 'http://cdn.xx.online/static/'
STATIC_URL = '/static/'
# STATIC_ROOT = 'static'

# 使得html文件能够读取静态的CSS\JS文件
HERE = os.path.dirname(os.path.abspath(__file__))
HERE = os.path.join(HERE, '../')
STATICFILES_DIRS = (
    os.path.join(HERE, 'static/'),
)

# SIMPLEUI主题设置
# 显示服务器信息
SIMPLEUI_HOME_INFO = True
# 隐藏最近动作
SIMPLEUI_HOME_ACTION = False
# 自定义Logo
# SIMPLEUI_LOGO = ''
# 离线模式
# SIMPLEUI_STATIC_OFFLINE = True


# 阿里云 CDN 存储静态资源文件 & 阿里云存储上传的图片/文件
# STATICFILES_STORAGE = 'django_oss_storage.backends.OssStaticStorage'

DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'

# AliCloud access key ID
OSS_ACCESS_KEY_ID = ''
# AliCloud access key secret
OSS_ACCESS_KEY_SECRET = ''
# 存储文件的bucket name
OSS_BUCKET_NAME = ''

# The URL of AliCloud OSS endpoint
# Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
OSS_ENDPOINT = 'oss-cn-guangzhou.aliyuncs.com'


## celery setting
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'  # redis:6379 的redis是docker-compose中对redis定义的服务名
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_beat.log")

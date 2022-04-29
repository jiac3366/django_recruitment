from .base import *

ALLOWED_HOSTS = ['127.0.0.1', "*", "host.docker.internal"]

DEBUG = False

# ---------------------
DINGTALK_WEB_HOOK = 'https://oapi.dingtalk.com/robot/send?access_token=84fb7e154150e5e67c02ac1b742fc365033f3d44a1d69a2801e47e37dacd936d'

# CDN的域名 http://cdn.jiac.online
# STATIC_URL = 'http://cdn.jiac.online/static/'
STATIC_URL = '/static/'
STATIC_ROOT = 'static'

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
OSS_ACCESS_KEY_ID = 'LTAI4FzpS9KeewAdf6kQ2CX3'
# AliCloud access key secret
OSS_ACCESS_KEY_SECRET = '2vDpyZUBW1jltHwko8eizl2LVbqo25'
# The name of the bucket to store files in
OSS_BUCKET_NAME = 'meetingrooms'

# The URL of AliCloud OSS endpoint
# Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
OSS_ENDPOINT = 'oss-cn-guangzhou.aliyuncs.com'

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_beat.log")

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# sentry_sdk.init(
#     dsn="http://xxx@recruit.ihopeit.com:9000/2",
#     integrations=[DjangoIntegration()],
#     # performance tracing sample rate, 采样率, 生产环境访问量过大时，建议调小（不用每一个URL请求都记录性能）
#     traces_sample_rate=1.0, #
#
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     # 聚类分析 可以上传它的浏览器 版本 操作系统
#     send_default_pii=True
# )

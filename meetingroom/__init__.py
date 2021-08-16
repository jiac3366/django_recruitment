from __future__ import absolute_import, unicode_literals
# from __future__ import absolute_import:避免导入的包有命名冲突

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)  # 暴露出去


import pymysql
pymysql.install_as_MySQLdb()
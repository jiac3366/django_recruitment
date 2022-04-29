from __future__ import absolute_import, unicode_literals

import os

from celery import Celery, shared_task

# set the default Django settings module for the 'celery' program.
# 如果没有修改settings文件路径的话 一般就是 根应用.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('meetingroom')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# 规定在settings中以CELERY开头的变量才能被celery读取
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# 自动从加载的app寻找task.py
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


#
# 设置定时任务的方式
# 1 django后台添加
# 2 系统启动完后自动注册 setup_periodic_tasks函数
# 3 在代码里直接配置 app.conf.beat_schedule
# 4 动态添加（较多） notes有截图


from celery.schedules import crontab

# this is important to load the celery tasks
from meetingroom.tasks import add

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'meetingroom.tasks.add',
        'schedule': 10.0,
        'args': (16, 4,)
    },
}


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='hello every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)


app.conf.timezone = "Asia/Shanghai"

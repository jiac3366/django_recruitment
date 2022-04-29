from celery import Celery

app = Celery('tasks', backend='redis://127.0.0.1', broker='redis://127.0.0.1')
# backend异步任务运行的结果的存储  存储任务的系统的代理


@app.task
def add(x, y):
    return x + y

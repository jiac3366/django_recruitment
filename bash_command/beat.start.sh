# DJANGO_SETTINGS_MODULE=settings.local celery -A meetingroom beat
DJANGO_SETTINGS_MODULE=settings.local celery -A meetingroom beat --scheduler django_celery_beat.schedulers:DatabaseScheduler

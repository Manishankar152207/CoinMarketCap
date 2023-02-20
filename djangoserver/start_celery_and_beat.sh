kill -9 $(ps aux | grep celery | grep -v grep | awk '{print $2}' | tr '\n'  ' ') > /dev/null 2>&1
celery -A djangoserver worker --concurrency=1 -l info --logfile=celery.log --detach
celery -A djangoserver beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler --detach
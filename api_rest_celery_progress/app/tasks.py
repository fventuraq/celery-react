'''
from celery import Celery
import time

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task
def long_task(task_id):
    total = 100
    for i in range(total):
        time.sleep(0.1)
        long_task.update_state(state='PROGRESS', meta={'current': i, 'total': total})
    return {'current': 100, 'total': 100, 'status': 'Task completed!', 'result': 42}
    '''

from celery import Celery
import time

app = Celery('api_rest_celery_progress', broker='redis://localhost:6379/0')

@app.task
def long_task(task_id):
    # Código de la tarea que tarda mucho
    total = 100
    for i in range(total):
        time.sleep(0.1)
        long_task.update_state(state='PROGRESS', meta={'current': i, 'total': total})
    return {'current': 100, 'total': 100, 'status': 'Task completed!', 'result': 42}
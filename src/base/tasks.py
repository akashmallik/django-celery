from time import sleep

from celery import shared_task
from celery_progress.backend import ProgressRecorder


@shared_task(bind=True)
def sleepy(self, seconds):
    progress_recorder = ProgressRecorder(self)
    result = 0
    for i in range(seconds):
        sleep(1)
        result += i
        progress_recorder.set_progress(i + 1, seconds, f'On iteration { i }')
    return None

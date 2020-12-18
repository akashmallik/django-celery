from django.shortcuts import render

from .tasks import sleepy


def index(request):
    result = sleepy.delay(25)
    return render(request, 'index.html', context={'task_id': result.task_id})

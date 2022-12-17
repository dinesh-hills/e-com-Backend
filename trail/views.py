from django.shortcuts import render
from .tasks import test_worker_task


def test_view(request):
    test_worker_task.delay('etst')
    return render(request, 'index.html', {'name': 'Dinesh'})
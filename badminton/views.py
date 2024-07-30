from django.shortcuts import render
from .tasks import score_difference, total_score
from celery.result import AsyncResult


def home(request):
    # Enqueue task using delay
    diff = score_difference.delay(10, 12)
    # Enqueue task using apply_async
    total = total_score.apply_async(args=[15, 20])
    context = {'total_id': total.id, 'diff_id': diff.id}
    print('Score Difference: ', diff)
    print('Total Score: ', total)
    return render(request, template_name='home.html', context=context)


def result(request, task_id):
    res = AsyncResult(task_id)
    print('Ready: ', res.ready())
    print('Successful: ', res.successful())
    print('Failed: ', res.failed())
    print('RESULT: ', res)
    return render(request, template_name='result.html', context={'result': res})

import time
from celery import shared_task


@shared_task
def test_worker_task(message):
    print('sending email to all the customers.')
    print(message)
    time.sleep(10)
    print('Emails were successfully sent!')
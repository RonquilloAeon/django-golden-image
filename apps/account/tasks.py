from __future__ import absolute_import
from celery import shared_task
import time


@shared_task
def test_task(value):
    """
    Dummy task. Sleeps to simulate processing
    :param value: int value
    :return: value + 1
    """
    time.sleep(2)

    return int(value) + 1

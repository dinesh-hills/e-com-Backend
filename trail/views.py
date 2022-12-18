from django.shortcuts import render
from django.views.generic import TemplateView
import logging

logger = logging.getLogger(__name__)

def test_view(request):
    try:
        logger.info('rendering template')
        data = {
            'name': 'Dinesh'
        }
        return render(request, 'trail/index.html', data)
    except ValueError as e:
        logger.error(e)
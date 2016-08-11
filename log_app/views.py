from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse, redirect
from log_app.models import LogModel
import logging
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger('test_logger')


@csrf_exempt
def index(request):
    if request.GET:
        logger.info('IM IN INDEX')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            LogModel.objects.create(log_name=request.POST['name'],
                                    log_sender=user.username,
                                    log_level=request.POST['level'],
                                    log_time=request.POST['time'],
                                    log_message=request.POST['msg'],
            )
            return redirect('admin/')